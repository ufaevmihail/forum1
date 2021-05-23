from django import forms


class AuthenticationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    #def get_user(self):
       # return auth.authenticate(username=self.username, password=


class CommentForm(forms.Form):
    comment_field = forms.CharField(widget=forms.Textarea)


class RubricForm(forms.Form):
    name = forms.CharField()

class ArticleForm(forms.Form):
    article_name = forms.CharField()
    comment_field = forms.CharField(widget=forms.Textarea)


class RegistrationForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField()
    password_confirm = forms.CharField(widget=forms.PasswordInput)