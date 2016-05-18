# coding:utf-8
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
            student_id = login_form.cleaned_data['student_id']
            password = login_form.cleaned_data['password']
            data = {'username': student_id, 'password': password}
            result, token = login_post(login_api, data)
            if result:
                if Account.check_user_exist(student_id):
                    user, account_password = Account.account_update_user(student_id)
                    account_user = Account(user=user,
                                           token=token)
                    account_user.save()
                    messages.add_message(request, messages.SUCCESS, u"Welcome Back")
                else:
                    info_api = settings.INFO_API
                    result, username = get_info(info_api, token, student_id)
                    user, account_password = Account.account_create_user(username)
                    account_user = Account(user=user,
                                           student_id=student_id,
                                           token=token)
                    account_user.save()
                    messages.add_message(request, messages.SUCCESS, u"Welcome to OAsystem")
                    return HttpResponseRedirect('/message/')
            else:
                messages.add_message(request, messages.ERROR, result)
                return HttpResponseRedirect('/message/')
    else:
        login_form = LoginForm()
    return render(request, 'account/login.html', {'login_form': login_form})