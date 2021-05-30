from django.conf.urls import url
from myforum.topic_views import template_views,action_views
from myforum.rubric_views import templ_views,act_views
from myforum.registration_views import registration_views

urlpatterns = [
    url(r'^$',templ_views.main_red),
    url(r'^main/$', templ_views.main_rubr),
    url(r'^topic/commentform/$', template_views.CommentPost.as_view()),
    url(r'^logout/$', template_views.logout, name ='logout'),
    url(r'^topic/(\d+)$', template_views.topic_view, name ="topic"),
    url(r'^ban/(\d+)/(\d+)$',action_views.BanView.as_view()),
    url(r'^unban/(\d+)/(\d+)$',action_views.UnbanView.as_view()),
    url(r'^mm/(\d+)/(\d+)$',action_views.MakeModer.as_view()),
    url(r'^unmode/(\d+)/(\d+)$',action_views.Unmode.as_view()),
    url(r'^rubric/(\d+)$', templ_views.rubric_view),
    url(r'createchetotam/(\d+)$',act_views.CreateArticleView.as_view()),
    url(r'^registration/$',registration_views.RegistrationView.as_view(),name='registration'),
    url(r'^registration/check_l/$',registration_views.same_login),
    url(r'^registration/check_e/$',registration_views.same_email),
#    url(r'^registration/test/$',registration_views.test_json),
    url(r'^verification/(\d+)/(\S+)',registration_views.verification_view),
    url(r'^make_verif/(\d+)',registration_views.make_verif),
    ]
