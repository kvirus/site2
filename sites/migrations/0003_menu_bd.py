# Generated by Django 4.1.7 on 2023-06-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_add_links_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu_bd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('link', models.CharField(max_length=250, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
    ]