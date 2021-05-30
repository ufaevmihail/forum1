from django.http import HttpResponseRedirect
from django.contrib import auth
from forum.forms import AuthenticationForm


def LoginFormMiddleware(get_response):

    def process_request(request,*args):
        #print('ffff')
        request.not_found = False
        request.not_active_user = False
        # if the top login form has been posted
        if request.method == 'POST' and 'logout' in request.POST:
            auth.logout(request)
        if request.method == 'POST' and 'is_top_login_form' in request.POST:
            # validate the form
            #print('ffff')
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                # log the user in
                from django.contrib.auth import login
                user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
                if user is not None and user.is_active:
                    if not user.userproperties.verified:
                        request.not_active_user = user
                    else:
                        login(request, user)
                else:
                    request.not_found = True



                # if this is the logout page, then redirect to /
                # so we don't get logged out just after logging in
                if '/account/logout/' in request.get_full_path():
                    return HttpResponseRedirect('/')

        else:
            form = AuthenticationForm()

        # attach the form to the request so it can be accessed within the templates

        request.login_form = form
        return get_response(request,*args)
    return process_request