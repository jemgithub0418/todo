# Generated by Django 3.1.7 on 2021-03-17 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20210318_0253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]
