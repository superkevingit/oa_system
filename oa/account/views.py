# coding=utf-8
from django.shortcuts import HttpResponseRedirect, render
from django.contrib import messages
from django.conf import settings
from .forms import LoginForm
from .models import Account
from .user_center import login_post, get_info


def account_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        login_api = settings.LOGIN_API
        if login_form.is_valid():
            student_id = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print student_id, password
            data = {'username': student_id, 'password': password}
            login_result, token = login_post(login_api, data)
            if login_result:
                print Account.check_user_exist(student_id)
                if Account.check_user_exist(student_id):
                    user, account_password = Account.account_update_user(student_id)
                    account_user = Account(user=user)
                    account_user.update(token=token)
                    messages.add_message(request, messages.SUCCESS, u"Welcome Back")
                    return HttpResponseRedirect('/message/')
                else:
                    info_api = settings.INFO_API
                    info_result, username = get_info(info_api, token, student_id)
                    user, account_password = Account.account_create_user(student_id)
                    account_user = Account(user=user,
                                           student_name=username,
                                           token=token)
                    account_user.save()
                    messages.add_message(request, messages.SUCCESS, u"Welcome to OAsystem")
                    return HttpResponseRedirect('/message/')
            else:
                messages.add_message(request, messages.ERROR, login_result)
                return HttpResponseRedirect('/login/')
    else:
        login_form = LoginForm()
    return render(request, 'account/login.html', {'login_form': login_form})
