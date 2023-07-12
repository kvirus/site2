# Generated by Django 4.1.7 on 2023-06-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_menu_bd'),
    ]

    operations = [
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=250, verbose_name='Телефон')),
                ('job', models.CharField(max_length=250, verbose_name='Должность')),
                ('mail', models.CharField(max_length=250, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Добавить телефон',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
