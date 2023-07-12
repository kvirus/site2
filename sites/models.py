from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class add_links(models.Model):
    title = models.CharField('Название', max_length=30)
    link = models.CharField('Ссылка', max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

class menu_bd(models.Model):
    title = models.CharField('Название', max_length=30)
    link = models.CharField('Ссылка', max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

class phone(models.Model):
    title = models.CharField('ФИО', max_length=30)
    phone = models.CharField('Телефон', max_length=250)
    job = models.CharField('Должность', max_length=250)
    mail = models.CharField('Почта', max_length=250)
    photo = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Добавить телефон'
        verbose_name_plural = 'Сотрудники'

    # def search(self, seach):
    #     qs = self.get_queryset()
    #     if seach:
    #         qs = qs.filter(Q(name__icontains=seach) | Q(description__icontains=seach))
    #     return qs

#Расширение стандарной модели админки
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username

# class MyUser(AbstractUser):
#      phone_number1 = models.CharField(max_length=20, blank=True)