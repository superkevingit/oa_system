# -*- coding:utf-8 -*-
from django.db import models
import hashlib


class Account(models.Model):
    db_table = "account"
    name = models.CharField(u"用户名", max_length=32)
    studentid = models.CharField(u"一卡通号", max_length=20)

    password = models.CharField(u"密码", max_length=50)
    tel = models.CharField(u"电话", max_length=50)
    mail = models.EmailField(u"邮箱", max_length=50)
    is_active = models.BooleanField(u"激活", default=1)

    def __str__(self):
        return self.name

    @classmethod
    def is_authenticated(self):
        return True

    @classmethod
    def hashed_password(self, password=None):
        if not password:
            return self.password
        else:
            return hashlib.md5(password).hexdigest()

    @classmethod
    def check_password(self, password):
        if self.hashed_password(password) == self.password:
            return True
        return False
