from django.conf.urls import include, url
from django.contrib import admin

from message.views import MessageListView, MessageDetailView, new_message

urlpatterns = [
    url(r'^message/$', MessageListView.as_view(), name='message-list'),
    url(r'^message/(?P<pk>\d+)/$', MessageDetailView.as_view(), name='message-datail'),
    url(r'^message/new$', new_message, name='message-new'),

    url(r'^admin/', include(admin.site.urls)),
]
