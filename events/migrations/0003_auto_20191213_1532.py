# Generated by Django 2.2.7 on 2019-12-13 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_shape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, null=True, related_name='events', to='events.Attendee'),
        ),
    ]