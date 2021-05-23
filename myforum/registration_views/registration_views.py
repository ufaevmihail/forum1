from django.shortcuts import render
from django.contrib import auth
from myforum.models import *
from forum.forms import RegistrationForm
from django.views.generic.base import View


class RegistrationView(View):
    def get(self,request):
        form = RegistrationForm()
        ctx={'form':form}
        return render(request,'registration/registration_form_template.html',context=ctx)
