from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=64)
    details = models.CharField(max_length=64)
    active = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(default=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.name

class Organizer(models.Model):
    name = models.CharField(max_length=64)
    details = models.CharField(max_length=64)
    mobile = models.CharField(max_length=32)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Category(models.Model): #Event Category
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"


class Attendee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    nid = models.CharField(max_length=14, db_index=True, unique=True)
    mobile = models.CharField(max_length=32)
    def __str__(self):
        return self.first_name


class Event(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, db_index=True)
    details = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True) #When Created Record
    certificate = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events') #Created by Record
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    attendees = models.ManyToManyField(Attendee, blank=True, null=True)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name='organizer', blank=True, null=True)

    class Meta:
        ordering = ('name',)
        index_together = ['id', 'slug']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)
        

class Loctimedate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventLocDates')
    day = models.DateField()
    location = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='venueDates')
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_timeslot = models.PositiveIntegerField(default = 1)
    reserved_timeslots = models.PositiveIntegerField(default = 1)
    def __str__(self):
        return self.event.name