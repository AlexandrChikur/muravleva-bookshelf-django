# Generated by Django 3.0 on 2022-05-19 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='books', to='users.Profile', verbose_name='Пользователи'),
        ),
    ]