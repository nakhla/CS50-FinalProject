# Generated by Django 2.2.7 on 2019-12-14 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20191213_1550'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Facility',
        ),
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, null=True, to='events.Attendee'),
        ),
    ]