# Generated by Django 2.2.7 on 2019-12-11 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('nid', models.CharField(db_index=True, max_length=14, unique=True)),
                ('mobile', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
                ('details', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('certificate', models.BooleanField(default=False)),
                ('shape', models.CharField(choices=[('L', 'Lines'), ('U', 'U shape'), ('R', 'Rounded tables')], default='L', max_length=1)),
                ('attendees', models.ManyToManyField(blank=True, null=True, to='events.Attendee')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='events.Category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('details', models.CharField(max_length=64)),
                ('mobile', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('details', models.CharField(max_length=64)),
                ('active', models.BooleanField(default=True)),
                ('capacity', models.PositiveIntegerField(default=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Loctimedate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_timeslot', models.PositiveIntegerField(default=1)),
                ('reserved_timeslots', models.PositiveIntegerField(default=1)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventLocDates', to='events.Event')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venueDates', to='events.Venue')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organizer', to='events.Organizer'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterIndexTogether(
            name='event',
            index_together={('id', 'slug')},
        ),
    ]
