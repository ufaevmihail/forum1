from myforum.models import *
from myforum.dynamic.rubric_composer import RubricComposer
from django.shortcuts import render,HttpResponseRedirect
from myforum.middleware import LoginFormMiddleware
def main_red(request):
    return HttpResponseRedirect('/main')

def main_rubr(request):
    return rubric_view(request,1)

@LoginFormMiddleware
def rubric_view(request,rubric_id):
    if rubric_id == '1':
        return HttpResponseRedirect('/main')
    user = request.user
    rubric = Rubric.objects.get(pk=rubric_id)
    comp = RubricComposer(user,rubric)
    #ctx = {"rubric_list":comp.compose_rubric_list(),"article_list":comp.compose_article_list()}
    ctx = {"composer":comp}
    return render(request,"rubric_template.html",context=ctx)