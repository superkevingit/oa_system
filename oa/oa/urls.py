from django.conf.urls import include, url
from django.contrib import admin

from message.views import OaMessageListView, OaMessageDetailView, new_oa_message, del_oa_message, undo_del_oa_message
from account.views import account_login

urlpatterns = [
    url(r'^message/$', OaMessageListView.as_view(), name='oa-message-list'),
    url(r'^message/(?P<pk>\d+)/$', OaMessageDetailView.as_view(), name='oa-message-datail'),
    url(r'^message/new/$', new_oa_message, name='oa-message-new'),
    url(r'^message/del/(\d+)/$', del_oa_message, name='oa-message-del'),
    url(r'^message/undo_del/(\d+)$', undo_del_oa_message, name='oa-message-del-undo'),
    url(r'^login/$', account_login, name='account-login'),

    url(r'^admin/', include(admin.site.urls)),
]
