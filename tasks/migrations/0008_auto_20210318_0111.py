# Generated by Django 3.1.7 on 2021-03-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20210318_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='batch',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
    ]
