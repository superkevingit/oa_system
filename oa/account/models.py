# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from random import choice
import string


class Account(models.Model):
    user = models.OneToOneField(User)
    student_name = models.CharField(u'姓名', max_length=20)
    token = models.CharField(u'密令', max_length=255)

    def __str__(self):
        return self.student_name.encode('utf-8')

    @classmethod
    def _MakePassword(cls, length=8, chars=string.letters+ string.digits):
        return ''.join([choice(chars) for i in range(length)])

    @classmethod
    def account_create_user(cls, student_id):
        account_password = cls._MakePassword()
        user = User(username=student_id)
        user.set_password(account_password)
        user.save()
        return user, account_password

    @classmethod
    def account_update_user(cls, student_id):
        account_password = cls._MakePassword()
        user = User(student_id=student_id)
        user.set_password(account_password)
        user.save()
        return user, account_password

    @classmethod
    def check_user_exist(cls, student_id):
        check_user = User.objects.filter(username=student_id)
        if check_user:
            return True
        else:
            return False
