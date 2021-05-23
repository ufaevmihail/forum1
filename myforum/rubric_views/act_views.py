from myforum.models import *
from django.utils import timezone
from django.views.generic.base import View
from myforum.dynamic.rubric_composer import get_user_status
from forum.forms import CommentForm,ArticleForm,RubricForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

class CreateArticleView(View):

    def get(self,request,id):
       # print(request.GET)
        class_=request.GET["class"].split()[1]
       # print(class_)
        if class_ == "create_rubric":
            ctx = {"form":RubricForm(),"id":id,"class":class_}
            return render(request,"create_rubric_form.html",context=ctx)
        if class_ == "create_article":
            ctx = {"form":ArticleForm(),"id":id,"class":class_}
            return render(request,"create_article_form.html",context=ctx)

    def post(self,request,id):
        father_rubric = Rubric.objects.get(pk=id)
        banned = father_rubric.banned.all()
        moders = father_rubric.moders.all()
        user_status = get_user_status(banned,moders,request.user)
        if request.POST["create_form"]=="create_rubric":
            if user_status.lvl > 0:
                Rubric.objects.create(user=request.user,name=request.POST['name'],parent=father_rubric)
                return HttpResponseRedirect(f"/rubric/{id}")
            else:
                return HttpResponseRedirect(f"/rubric/{id}")
        if request.POST["create_form"]=="create_article":
            if user_status.lvl > 1:
                Theme.objects.create(user = request.user,name=request.POST['article_name'],
                                     text=request.POST['comment_field'],rubric=father_rubric)
                return HttpResponseRedirect(f"/rubric/{id}")
            else:
                return HttpResponseRedirect(f"/rubric/{id}")


