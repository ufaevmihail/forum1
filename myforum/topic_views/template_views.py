from django.shortcuts import render
from django.contrib import auth
from myforum.models import *
from django.views.generic.base import View
from myforum.dynamic.Composer import ThemeComposer
from forum.forms import CommentForm
from django.http import HttpResponseRedirect
from myforum.middleware import LoginFormMiddleware
# Create your topic_views here.


def index1(request):
    return topic_view(request,1)


def index(request):
    id = request.GET['id']
    class_=request.GET['class']
    ctx = {'form':CommentForm(),'id':id,'class_':class_}
    return render(request,'comment_form.html',ctx)


class CommentPost(View):

    def get(self,request):
        id = request.GET['id']
        class_ = request.GET['class']
        ctx = {'form': CommentForm(), 'id': id, 'class_': class_}
        return render(request, 'comment_form.html', ctx)

    def post(self,request):
        params = request.POST
        if params['parent_class']=='article_body':
            coment_parent = None
            article = Theme.objects.get(pk=params['parent_id'])
        else:
            coment_parent_id = params['parent_id']
            coment_parent=Comment.objects.get(pk=coment_parent_id)
            article = coment_parent.theme
        new_comment = Comment.objects.create(user=request.user,theme=article,parent=coment_parent,text=request.POST['comment_field'])
        new_comment.update_state()
        return HttpResponseRedirect(f"/topic/{article.id}")


def logout(request):
    auth.logout(request)

@LoginFormMiddleware
def topic_view(request,topic_id):
    user = request.user
    theme = Theme.objects.get(pk=topic_id)
    comp = ThemeComposer(user,theme)
    #data = { "article": comp.compose_article(), "comments" : comp.compose_comments() }
    data = {'comp':comp}
    '''qd = request.GET.copy()
    qd["lod"]='ff'
    request.GET = qd
    print(request.GET)'''
    #response = render(request,"topic_template.html",context = data)
    #response["lod"]='ff'
    #print(csrf.get_token(request))
    return render(request,"topic_template.html",context = data)