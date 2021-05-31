# Generated by Django 3.2.3 on 2021-05-31 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_name', models.CharField(max_length=50, verbose_name='Имя друга')),
                ('friend_city', models.CharField(max_length=100, verbose_name='Город проживания')),
            ],
        ),
        migrations.CreateModel(
            name='Icecream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название мороженого')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание мороженого')),
            ],
            options={
                'verbose_name_plural': 'Список Мороженого',
            },
        ),
    ]