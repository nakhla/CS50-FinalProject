from django.contrib import admin
from .models import Venue, Organizer, Category, Attendee, Event, Loctimedate

# Register your models here.
admin.site.register(Venue)
admin.site.register(Organizer)
admin.site.register(Category)


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nid', 'first_name', 'last_name', 'email', 'mobile')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ( 'name', 'id','category', 'organizer', 'created' )

@admin.register(Loctimedate)   
class LoctimedateAdmin(admin.ModelAdmin):
    list_display = ( 'event', 'event_id', 'id', 'day','location', 'start_time', 'end_time' )