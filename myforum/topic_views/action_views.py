
from django.http import HttpResponseRedirect
from myforum.models import *
from django.views.generic.base import View
from myforum.dynamic.rubric_composer import get_user_status


class BanView(View):
    lvl_difference = 1
    min_level = 2

    def legalization(self,ask_user_status,user_status):
        if (ask_user_status.lvl >= self.min_level) and ask_user_status.lvl-user_status.lvl >= self.lvl_difference:
            return True

    def action(self,user,rubric,theme_banned,theme_moders):
        if user not in rubric.banned.all():
            rubric.banned.add(user)

    def get(self,request,user_id,theme_id):
        ask_user = request.user
        if not ask_user.is_authenticated:
            return HttpResponseRedirect(f"/topic/{theme_id}")
        theme = Theme.objects.get(pk=theme_id)
        #theme_banned = [i.id for i in theme.rubric.banned.all()]
        theme_banned = theme.rubric.banned.all()
        #theme_moders = [i.id for i in theme.rubric.moders.all()]
        theme_moders =theme.rubric.moders.all()
        ask_user_status = get_user_status(theme_banned,theme_moders,ask_user)
        user = User.objects.get(pk=user_id)
        user_status = get_user_status(theme_banned,theme_moders,user)
        if self.legalization(ask_user_status,user_status):
            self.action(user,theme.rubric,theme_banned,theme_moders)
        return HttpResponseRedirect(f"/topic/{theme_id}")


class UnbanView(BanView):
    def action(self,user,rubric,theme_banned,theme_moders):
        if user in theme_banned:
            rubric.banned.remove(user)


class MakeModer(BanView):
    lvl_difference = 2
    min_level = 4

    def action(self, user, rubric,theme_banned,theme_moders):
        if user not in theme_moders:
            rubric.moders.add(user)


class Unmode(MakeModer):

    def action(self,user,rubric,theme_banned,theme_moders):
        if user in theme_moders:
            rubric.moders.remove(user)