# -*- coding:utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Message
from .forms import MessageForm


class MessageListView(ListView):
    model = Message

    def get_context_data(self, **kwargs):
        context = super(MessageListView, self).get_context_data(**kwargs)
        return context


class MessageDetailView(DetailView):
    model = Message

    def get_context_data(self, **kwargs):
        context = super(MessageDetailView, self).get_context_data(**kwargs)
        return context


def new_message(request):
    if request.method == 'POST':
        message_form = MessageForm(request.POST)

        if message_form.is_valid():
            Message.new_message(title=message_form.cleaned_data['title'],
                                content=message_form.cleaned_data['content'])
            return HttpResponseRedirect('/message/')
    else:
        message_form = MessageForm()
    return render(request, 'message/new_message.html', {'message_form': message_form})
