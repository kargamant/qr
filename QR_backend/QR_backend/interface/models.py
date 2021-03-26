from django.db import models


class teacher(models.Model):
    email = models.CharField('адрес электронной почты', max_length=100)
    password = models.CharField('пароль', max_length=100)





