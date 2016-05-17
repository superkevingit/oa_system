from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned, DoesNotExist
from random import choice
import string


class Account(models.Model):
    user = models.OneToOneField(User)
    student_id = models.CharField(u'学号', max_length=20)
    tokens = models.CharField(u'密令')

    def __str__(self):
        return self.user.username

    def _MakePassword(length=8, chars=string.letters+ string.digits):
        return ''.join([choice(chars) for i in range(length)])

    @classmethod
    def account_login_user(cls, student)

    @classmethod
    def account_create_user(cls, student_id, student_name):
        account_password = cls._MakePassword()
        user = cls(student_id=student_id)
        user.user.username = student_name
        user.user.set_password(account_password)
        user.save()
        return user, account_password

    @classmethod
    def account_update_user(cls, student_id):
        account_password = cls._MakePassword()
        user = cls(student_id=student_id)
        user.user.set_password(account_password)
        user.save()
        return user, account_password

    @classmethod
    def check_user_exist(cls, student_id):
        try:
            cls.objects.filter(student_id=student_id)
        except MultipleObjectsReturned:
            return True
        except DoesNotExist:
            return False
        else:
            return True
