from django.urls import path
from name_filter.views import user_input,home

urlpatterns=[
  path('',home,name='home'),
  path("api/checkname/",user_input,name="user_input"),
]