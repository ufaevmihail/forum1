class CommentButtonAttribs:
    text = "коментировать"
    onclick = ""
    button_class = "\"comment\""

class CommentButton:
    button_template = "<button {0} class={1}>{2}</button>"
    attribs = CommentButtonAttribs()

    href = ""

    def __init__(self,theme):
        self.theme = theme

    def string_html(self,asking_user_status,user,user_status,rubric,*args):
#        function_arg = f'this'
        #self.attribs.onclick = self.attribs.onclick.format(function_arg)
        if self.attribs.onclick:
            self.href = self.attribs.onclick.format(user, self.theme.id)
        return self.button_template.format(self.href,self.attribs.button_class,self.attribs.text)


class RazbanButtonAttribs:
    text = "разбанить"
    onclick = "onclick=\"window.location.href='/unban/{}/{}'\""
    button_class = "\"button\""


class RazbanButton(CommentButton):
    attribs = RazbanButtonAttribs()


class BanButtonAttribs:
    text = "забанить"
    onclick = "onclick=\"window.location.href='/ban/{}/{}'\""
    button_class = "\"button\""
    other = RazbanButton
    list_number = 0


class UnmodeButtonAttribs:
    text = "анмоднуть"
    onclick ="onclick=\"window.location.href='/unmode/{}/{}'\""
    button_class = "\"button\""

class UnmodeButton(CommentButton):
    attribs = UnmodeButtonAttribs()


class MakeModerAttribs:
    text = "сделать модером"
    onclick = "onclick=\"window.location.href='/mm/{}/{}'\""
    button_class = "\"button\""
    other = UnmodeButton
    list_number = 1


def mm_check_func(obj,user_id,moders_id,banned_id):
    if user_id not in banned_id:
        if user_id not in moders_id:
            return 1
        if user_id in moders_id:
            return 2


def ban_check_func(obj,user_id,moders_id,banned_id):
    if user_id not in banned_id:
        return 1
    if user_id in banned_id:
        return 2



'''class PermButton(CommentButton):
    attribs = None

    def string_html(self,asking_user_status,user,user_status,rubric,*args):
        check_list= args[self.attribs.list_number]
        
        if user not in check_list:
            return super().string_html(asking_user_status,user,user_status,rubric,*args)
        else:
            return self.attribs.other(self.theme).string_html(asking_user_status,user,user_status,rubric,*args)'''


class PermButton(CommentButton):
    attribs = None
    check_func = None

    def string_html(self, asking_user_status, user, user_status, rubric, *args):
        check_list = args[self.attribs.list_number]
        check = self.check_func(user,args[1],args[0])
        if not check:
            return ""
        else:
            if check == 1:
                return super().string_html(asking_user_status, user, user_status, rubric, *args)
            else:
                return self.attribs.other(self.theme).string_html(asking_user_status, user, user_status, rubric, *args)


class EmpoweredOption:
    lvl_adventage = 0
    button_type = None
    def __init__(self,theme):
        self.theme = theme

    def string_html(self,asking_user_status,user,user_status,rubric,*args):
        if asking_user_status.lvl - user_status.lvl > self.lvl_adventage:
            return self.button_type(self.theme).string_html(asking_user_status,user,user_status,rubric,*args)
        else:
            return ""


class BanButton(PermButton):
    attribs = BanButtonAttribs()
   # href = "href=\"/ban/{}/{}\""
    check_func = ban_check_func



class MakeModerButton(PermButton):
    attribs = MakeModerAttribs()
    check_func = mm_check_func
  #  href = "href=\"/mm/{}/{}\""

class Ban(EmpoweredOption):
    lvl_adventage = 0
    button_type = BanButton


class MakeModer(EmpoweredOption):
    lvl_adventage = 1
    button_type = MakeModerButton















'''if __name__ == "__main__":
    print(Ban().string_html(Admin(),2,Moderator(),2,[1,3,4],[10,22]))
    print(MakeModer().string_html(Admin(), 6, SimpleUser(), 2, [1, 3, 4],[10,22]))
    print(CommentButton().string_html(Admin(), 6, SimpleUser(), 2, [1, 3, 4], [10, 22]))'''











