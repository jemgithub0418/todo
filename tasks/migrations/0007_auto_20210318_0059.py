# Generated by Django 3.1.7 on 2021-03-17 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20210318_0050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'ordering': ['-batch'], 'verbose_name': 'Batch', 'verbose_name_plural': 'Batches'},
        ),
    ]
