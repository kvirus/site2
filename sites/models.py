from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class add_links(models.Model):
    title = models.CharField('Название', max_length=30)
    link = models.CharField('Ссылка', max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'