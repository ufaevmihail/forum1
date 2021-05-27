from django.shortcuts import render
from django.contrib import auth
from myforum.models import *
from forum.forms import RegistrationForm
from django.views.generic.base import View
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login
import re
#from django.http import JsonResponse
#from django.forms.models import model_to_dict


class RegistrationView(View):
    def get(self,request):
        form = RegistrationForm()
        ctx={'form':form}
        return render(request,'registration/registration_form_template.html',context=ctx)

    def post(self,request):
      #  print(request.POST)
        username = request.POST['user_name']
        if not validate('user_name',username):
            return HttpResponseRedirect('/notname')
        email=request.POST['email']
        if not validate('email',email):
            return HttpResponseRedirect('/notemail')
        password=request.POST['password']
        if not validate('password',password):
            return HttpResponseRedirect('/notpassword')
        user=User.objects.create_user(username,email,password)
        userprops = UserProperties()
        user.userproperties=userprops
        user.userproperties.save()
        user = auth.authenticate(username=username, password=password)
#        if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect('/main/')



def same_login(request):
    new_login= request.GET['login']

    user = User.objects.filter(username=new_login)
   # print(user)
    if user:
        return HttpResponse("false")
    else:
        return HttpResponse("true")


def same_email(request):
    new_email= request.GET['email']

    email = User.objects.filter(email = new_email)
   # print(user)
    if email:
        return HttpResponse("false")
    else:
        return HttpResponse("true")


#def test_json(request):
#    article = Theme.objects.get(pk=1)
#    return JsonResponse(model_to_dict(article))
def validate(name,value):
    if not value:
        return False
    router = {'user_name':[lambda x: length_req(x,4),is_login_free],'email':[is_email,is_email_free],
              'password':[lambda x: length_req(x,8),has_Aa,has_9]}
    for i in router[name]:
        if not i(value):
            return False
    return True

def length_req(value,length):
    if len(value) >= length:
        return True


def is_login_free(value):
    user = User.objects.filter(username=value)
    if not user:
        return True


def is_email_free(value):
    user = User.objects.filter(email=value)
    if not user:
        return True


def is_email(value):
    match = re.match(r'\S+@\S+\.\S+',value).group(0)
  #  print(match)
    if match == value:
        return True

def has_Aa(value):
    result1=re.search(r'[A-Z]',value)
    result2=re.search(r'[a-z]',value)
    if result1.group(0) and result2.group(0):
        return True


def has_9(value):
    result = re.search(r'[0-9]',value)
    if result.group(0):
        return True










