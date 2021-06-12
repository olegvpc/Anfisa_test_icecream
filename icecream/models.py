# Наша "База данных"
# name (англ. "имя") - название мороженого
# description (англ. "описание") - описание мороженого
from django.db import models


class Icecream(models.Model):
    name = models.CharField(verbose_name="Название мороженого", max_length=100)
    description = models.TextField(verbose_name="Описание мороженого", max_length=200, blank=True)


    class Meta:
        verbose_name_plural = "Список Мороженого"

    def __str__(self):
        return self.name


class Friend(models.Model):
    friend_name = models.CharField(verbose_name="Имя друга", max_length=50)
    friend_city = models.CharField(verbose_name="Город проживания", max_length=100)
    friend_icecream = models.ForeignKey(Icecream, on_delete=models.SET_NULL, blank=True,
                              null=True, verbose_name="Любимые сорта мороженого", related_name="friends")

    class Meta:
        verbose_name_plural = "Список Друзей"

    def __str__(self):
        return self.friend_name
