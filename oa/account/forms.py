# encoding: utf-8
from django import forms


class LoginForm(forms.Form):
    student_id = forms.CharField(label=u'学号', max_length=20)
    u_password = forms.CharField(label=u'密码', widget=forms.PasswordInput())
