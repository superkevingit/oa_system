# -*- coding:utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse

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
    if mes and mes.is_active==True:
        OaMessage.del_message(id=int(id))
        info = reverse('oa-message-del-undo', args=[int(id)])
        messages.add_message(request, messages.SUCCESS, info)
        return HttpResponseRedirect('/message/')
    messages.add_message(request, messages.ERROR, u"del message failed")
    return HttpResponseRedirect('/message/')


def undo_del_oa_message(request, id):
    mes = OaMessage.objects.get(id=int(id))
    if mes and mes.is_active==False:
        OaMessage.undo_del_message(id=int(id))
        messages.add_message(request, messages.SUCCESS, 'success')
        return HttpResponseRedirect('/message/')
    messages.add_message(request, messages.ERROR, u"undo del message failed")
    return HttpResponseRedirect('/message/')
