# -*- coding:utf-8 -*-
from django.db import models


class OaMessage(models.Model):
    title = models.CharField(u"标题", max_length=50)
    writer = models.CharField(u"发布者", max_length=50)
    content = models.TextField(u"内容")
    pub_time = models.DateTimeField(u"发布时间", auto_now_add=True)
    mod_time = models.DateTimeField(u"修改时间", auto_now=True)
    is_active = models.BooleanField(u"是否删除", default=False)

    def __str__(self):
        return self.title

    @classmethod
    def new_message(cls, title, content):
        cls.objects.get_or_create(title=title, content=content)

    @classmethod
    def del_message(cls, mes_id):
        cls.objects.update_or_create(id=mes_id, is_active=True)

    @classmethod
    def undo_del_message(cls, mes_id):
        cls.objects.update_or_create(id=mes_id, is_active=False)
