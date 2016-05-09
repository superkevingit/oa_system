from django.conf.urls import include, url
from django.contrib import admin

from message.views import OaMessageListView, OaMessageDetailView, new_oa_message

urlpatterns = [
    url(r'^message/$', OaMessageListView.as_view(), name='oa-message-list'),
    url(r'^message/(?P<pk>\d+)/$', OaMessageDetailView.as_view(), name='oa-message-datail'),
    url(r'^message/new$', new_oa_message, name='oa-message-new'),

    url(r'^admin/', include(admin.site.urls)),
]
