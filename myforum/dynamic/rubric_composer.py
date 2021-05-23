from myforum.models import *
from myforum.dynamic.rubric_options import CreateRubric,CreateArticle

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


class RubricComposer:
    rubric_list_template = "<div class='rubric_list'><p> Рубрики </p>{}"
    articles_list_template = "<div class='articles_list'><p> Топики </p>{}"
    rubric_options = []
    rubric_options_global={"создать_рубрику": CreateRubric }
    topic_options = []
    topic_options_global = {"создать_тему": CreateArticle }

    def __init__(self,asking_user,rubric):
        self.rubric = rubric
        self.banned = self.rubric.banned.all()
        self.moders = self.rubric.moders.all()
        self.asking_user = asking_user
        self.asking_user_status = self.get_ask_user_status()

    def compose_back(self):
        if self.rubric.parent:
            return f"<span class='element back_rubric' href='/rubric/{self.rubric.parent.id}'> из рубрики {self.rubric.parent.name}</span>"
        else:
            return ""

    def get_ask_user_status(self):
        if not self.asking_user.is_authenticated:
            return Anonymous()
        else:
            return get_user_status(self.banned,self.moders,self.asking_user)

    def rubric_options_f(self,list_options,user=None):
        html_string = ""
        if user:
            user_status = get_user_status(self.banned,self.moders,user)
            for option in self.asking_user_status.options:
                if option in list_options:
                    html_string += list_options[option](self,self.asking_user_status,user,user_status).make_html()
        else:
            for option in list_options:
                html_string += list_options[option](self, self.asking_user_status, user, None).make_html()
        return html_string

    def compose_rubric_list(self):
        rubric_list_html = ""
        rubric_el = "<div class='r_element element' href='/rubric/{}'><span>{}</span><p class='author'>{}</p></div>"
        ch_rubrics = self.rubric.get_children()
        for rubric in ch_rubrics:
            rubric_list_html += rubric_el.format(rubric.id,rubric.name,rubric.user.username)\
                                +self.rubric_options_f(self.rubric_options,rubric.user)
        if not rubric_list_html:
            rubric_list_html = "<p> Здесь пока ничего нет </p>"
        return self.rubric_list_template.format(rubric_list_html
                                                + '</div>'+self.rubric_options_f(self.rubric_options_global))

    def compose_article_list(self):
        article_list_html = ""
        article_el = "<div class='art_element element' href='/topic/{}'><span>{} </span><p class='author'>{}</p></div>"
        articles = self.rubric.theme_set.all()
        for article in articles:
            article_list_html += article_el.format(article.id,article.name,article.user.username) \
                                 + self.rubric_options_f(self.topic_options,article.user)
        if not article_list_html:
            article_list_html = "<p> Здесь пока ничего нет, станьте первым </p>"
        return self.articles_list_template.format(article_list_html
                                                  + '</div>' + self.rubric_options_f(self.topic_options_global))


















def get_user_status(banned,moders,user):
    if user.userproperties.admin:
        return Admin()
    if user in banned:
        return Anonymous()
    if user in moders:
        return Moderator()
    else:
        return SimpleUser()
