from django.shortcuts import render
from django.http import JsonResponse,request
from django.views.decorators.csrf import csrf_exempt
import json
from .check_name import match_pattern,accuracy_of_name
from .models import UserName
# Create your views here.
def home(request):
  return render(request,'home.html')

bad_words=['sex','rape','onlyfans','fuck','xxx','cashapp','bitch','slut','porn','admin','support','bitcoin','0nlyfans','ass','asshole','boobs']

def alter_name(text): # This function is used to alter or filter the name from symbols like .,-,etc....
  return ''.join(c for c in text.lower() if c.isalnum())

def check_bad_word(name): # this function checks if the name contains in badword.
  name=alter_name(name)
  return any(word in name for word in bad_words)


@csrf_exempt
def user_input(request):
  if request.method == "POST":
    data=json.loads(request.body)
    name=data.get("name","")
    
    if not name:
      return JsonResponse({"status": "error", "reason": "Empty name not accepted"})
    
    if check_bad_word(name):
      return JsonResponse({"status": "rejected", "reason": "Not a Valid Name"})

    match=match_pattern(name)
    if match:
      return JsonResponse({"status": "rejected", "reason": "Not a Valid Name"})
      

    harmful=accuracy_of_name(name)
    if harmful:
      return JsonResponse({"status": "rejected", "reason": "Not a Valid Name"})
    
    UserName.objects.create(name=name)
    return JsonResponse({"status": "approved", "reason": "Name is created"})
  return JsonResponse({"status": "error", "reason": "Invalid method"}, status=405)
  
    
    