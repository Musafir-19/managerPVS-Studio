from django.db import models


class PassSave(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название учетки')
    email = models.TextField(verbose_name='Имя пользователя')
    password = models.TextField(verbose_name='Пароль')

    def __str__(self) -> str:
        return self.title