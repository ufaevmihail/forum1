class Option:
    min_lvl=1
    requirements = []
    condition_to_alt = lambda x,y: False
    button = None
    alt_button = None

    def __init__(self,comp,asking_user_status,user,user_status,theme=None):
        self.theme = theme
        self.comp = comp
        self.user=user
        if user:
            self.user_id=user.id
        else:
            self.user_id = 0
        self.asking_user_status = asking_user_status
     #   print(asking_user_status)
        self.user_status = user_status

    def make_html(self):
        if self.asking_user_status.lvl < self.min_lvl:
            return ""
        for req in self.requirements:
            if not req(self.asking_user_status,self.user_status,self.comp.rubric,self.user,self.comp):
                return ""
        if self.condition_to_alt(self.comp):
            self.button = self.alt_button
        return self.button(self.user_id,self.comp.rubric,self.theme).make_html()


class Button:
    template_html = "<span {} class='button{}' > {} </span>"
    class_= ""
    value = ""

    def __init__(self,user_id,rubric,theme):
        self.theme=theme
        self.rubric=rubric
        self.user_id = user_id

    def make_html(self):
        return self.template_html.format(self.make_action(),self.class_,self.value)

    def make_action(self):
        return ""


class RubricCreateButton(Button):
    class_ = " create_rubric"
    value = "создать рубрику"


class CreateRubric(Option):
    min_lvl = 2
    button = RubricCreateButton


class ArticleCreateButton(Button):
    class_ = " create_article"
    value = "создать топик"


class CreateArticle(Option):
    min_lvl = 1
    button = ArticleCreateButton


class BanButton(Button):
    class_ = ""
    value = "забанить"

    def make_action(self):
        return f"onclick=window.location.href='/ban/{self.user_id}/{self.theme}'"         #переделать


class UnbanButton(Button):
    class_ = ""
    value = "разбанить"

    def make_action(self):
        return f"onclick=window.location.href='/unban/{self.user_id}/{self.theme}'"


def average_req(ask_user_status,user_status,rubric,user,comp):
    if ask_user_status.lvl > user_status.lvl:
        return True


def banned_req(ask_user_status,user_status,rubric,user,comp):
    if user.id not in comp.theme_banned:
        return True


def ban_cond_to_alt(opt,comp):
    if opt.user_id in comp.theme_banned:
        return True



class Ban(Option):
    min_lvl = 2
    button = BanButton
    requirements = [average_req]
    condition_to_alt = ban_cond_to_alt
    alt_button = UnbanButton


class MakeModerButton(Button):
    class_ = ""
    value = "сделать модером"

    def make_action(self):
        return f"onclick=window.location.href='/mm/{self.user_id}/{self.theme}'"


class UnmodeButton(Button):
    class_ = ""
    value = "анмоднуть"

    def make_action(self):
        return f"onclick=window.location.href='/unmode/{self.user_id}/{self.theme}'"


class MakeModer(Option):
    min_lvl = 4
    button = MakeModerButton
    requirements = [average_req,banned_req]
    condition_to_alt = lambda x,y: True if x.user_id in y.theme_moders else False
    alt_button = UnmodeButton


class CommentButton(Button):
    class_ = " comment"
    value = "коментировать"


class ToComment(Option):
    min_lvl = 1
    button = CommentButton





















