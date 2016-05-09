# -*- coding:utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from .models import OaMessage
from .forms import OaMessageForm


class OaMessageListView(ListView):
    model = OaMessage

    def get_context_data(self, **kwargs):
        context = super(OaMessageListView, self).get_context_data(**kwargs)
        return context


class OaMessageDetailView(DetailView):
    model = OaMessage

    def get_context_data(self, **kwargs):
        context = super(OaMessageDetailView, self).get_context_data(**kwargs)
        return context


def new_oa_message(request):
    if request.method == 'POST':
        message_form = OaMessageForm(request.POST)
        if message_form.is_valid():
            OaMessage.new_message(title=message_form.cleaned_data['title'],
                                  content=message_form.cleaned_data['content'])
            messages.add_message(request, messages.SUCCESS, u"add pubmessage success")
            return HttpResponseRedirect('/message/')
    else:
        message_form = OaMessageForm()
    return render(request, 'message/new_message.html', {'message_form': message_form})


def del_oa_message(request, id):
    mes = OaMessage.objects.get(id=int(id))
    if mes:
        OaMessage.del_message(id=int(id))
        messages.add_message(request, messages.SUCCESS, u"del success")
        return HttpResponseRedirect('/message/')
    return messages.add_message(request, messages.ERROR, u"del message failed")


















