# Generated by Django 2.2.7 on 2019-12-11 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='shape',
        ),
    ]
