import re
from profanity_check import predict_prob,predict
 
#check the name patterns like c@shapp,c@sh @pp,etc....
patterns=[
  r"(c[a@][s$]h ?[@a]pp)", 
  r"([o0]nly ?f[a@]n[s$])",
  r"\b(admin|support)\b",
  r"(s[e3]x+|f[\W_]*u[\W_]*c[\W_]*k)",
  r"(p[o*0]rn)",
  r"[a@][s$]*h[0o][l1]e",
  r"[Bb][0o]*[bB][s$]",
  r"b[i1]tch"
]

def match_pattern(name): # this function used to checks the what kind of pattern is this.
  name=name.lower()
  for pattern in patterns:
    if re.search(pattern,name):
      return True
  return False

def accuracy_of_name(name,limit=0.6):  #this function is used to checks the accuracy of the name if its greater than 0.6 its conforms its an inappropriate name.
  accuracy=predict_prob([name])[0]
  return accuracy > limit