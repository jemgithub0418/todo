# Generated by Django 3.1.7 on 2021-03-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20210318_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Batch',
                'verbose_name_plural': 'Batches',
                'ordering': ['-batch'],
            },
        ),
        migrations.RemoveField(
            model_name='task',
            name='batch',
        ),
        migrations.AddField(
            model_name='task',
            name='batch',
            field=models.ManyToManyField(to='tasks.Batch'),
        ),
    ]