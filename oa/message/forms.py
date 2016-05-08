# encoding: utf-8
from django import forms


class MessageForm(forms.Form):
    title = forms.CharField(label=u'公告标题', max_length=50)
    content = forms.CharField(label=u'公告内容')
