#from myforum.dynamic.options import Ban,MakeModer,CommentButton
from myforum.dynamic.rubric_options import Ban,MakeModer,ToComment
from myforum.models import *
'''class Admin:
    lvl = 4
    options = ("коментировать","забанить","повысить")


class Moderator:
    lvl = 2
    options = ("коментировать","забанить")


class SimpleUser:
    lvl = 1
    options = ("коментировать",)


class Anonymous:
    lvl = 1
    options = []'''
class Admin:
    lvl = 4
    options = ("коментировать","забанить","повысить","создать_тему","создать_рубрику")


class Moderator:
    lvl = 2
    options = ("коментировать","забанить","создать_тему","создать_рубрику")


class SimpleUser:
    lvl = 1
    options = ("коментировать","создать_тему")

class Anonymous:
    lvl = 0
    options = []


class ThemeComposer:

    article_template = "<div class='article_body' id={}><p>{}</p><p class='quoute_text'>{}</p><p>{}</p><p>{}</p>"
    comment_template = "<div class='comment_body'><div class='comment_quote' id={}><p class='quoute_text'>{}</p><p>{}</p>"
    options = {"коментировать":ToComment, "забанить":Ban, "повысить":MakeModer}

    def __init__(self,user,theme):
        self.theme=theme
        self.theme_moders = []
        self.rubric = self.theme.rubric
        self.theme_comments_query = Comment.objects.filter(theme=theme)
        for i in self.rubric.moders.all():
            self.theme_moders.append(i.id)
        self.theme_banned = []
        for i in self.rubric.banned.all():
            self.theme_banned.append(i.id)
        self.comments_html=""
        self.asking_user_status = self.get_ask_user_status(user)

    def compose_back(self):
            return f"<span class='element back_rubric' href='/rubric/{self.rubric.id}'> рубрика {self.rubric.name}</span>"

    def compose_article(self):
        author = self.theme.user
        article_name = self.theme.name
        article_text = self.theme.text
        article = self.article_template.format(self.theme.id,article_name,article_text,author.username,self.theme.last_update)
        return article+self.ask_user_options(author)+"</div>"          #

    def compose_comments(self):
        #self.comments_query = self.theme.comment_set.all()
        self.comments_setter()
        return self.comments_html

    def comments_setter(self,parent=None):
        comments_query = self.theme_comments_query.filter(parent = parent)
        if comments_query:
            self.comments_html += "<div class=\"comments_container\">"
            for comment in comments_query:
                author = comment.user
                comment_str = self.comment_template.format(comment.id,comment.text,author.username)
                self.comments_html += comment_str+self.ask_user_options(author)+'</div>'
                self.comments_setter(comment.id)
                self.comments_html += "</div>"
            self.comments_html+="</div>"

    def ask_user_options(self,user):
        buttons_html=""
        user_status = get_user_status(self.theme_banned,self.theme_moders,user)
        for option in self.asking_user_status.options:
            if option in self.options:
                #buttons_html += self.options[option](self.theme).string_html(self.asking_user_status,user.id,
                                                                         #   user_status,self.theme.id,self.theme_banned,self.theme_moders)
               # print(Comment.__class__.__dict__)
                buttons_html += self.options[option](self,self.asking_user_status,user,user_status,self.theme.id).make_html()
        return buttons_html

    def get_ask_user_status(self, user):
        if not user.is_authenticated:
            return Anonymous()
        else:
            return get_user_status(self.theme_banned,self.theme_moders,user)


def get_user_status(theme_banned,theme_moders,user):
    if user.userproperties.admin:
        return Admin()
    if user.id in theme_banned:
        return Anonymous()
    if user.id in theme_moders:
        return Moderator()
    else:
        return SimpleUser()




if __name__ == "__main__":
    user = User.objects.get(pk=1)
    theme = Theme.objects.get(pk=1)
    comp = ThemeComposer(user,theme)
    print(comp.compose_article())
    #from datetime import date as dt        dt.today()





