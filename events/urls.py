from django.urls import path
from . import views


urlpatterns = [
      path("", views.index, name='index'),
      path("getResrvedLocationsByDay/", views.getResrvedLocationsByDay, name='getResrvedLocationsByDay'),
      path("insertReservedSlotsToEvent/", views.insertReservedSlotsToEvent, name='insertReservedSlotsToEvent'),
      path("booking/", views.booking, name='booking'),
      path("createEvent/", views.createEvent, name='createEvent'),
      path("<int:event_id>/attendees/", views.attendees, name='attendees'),
      path("addAttendee/", views.addAttendee, name="addAttendee"),
      path("checkifAttExists/", views.checkifAttExists, name="checkifAttExists"),
      path("delAttendee/", views.delAttendee, name="delAttendee"),
      path("editAttendee/", views.editAttendee, name="editAttendee"),
      path("updateAttendee/", views.updateAttendee, name="updateAttendee"),
      path("events/", views.events, name="events"),
      path("attendeesList/", views.attendeesList, name='attendeesList'),
      path("modifyAttendee/", views.modifyAttendee, name="modifyAttendee"),
      path("filterEvents/", views.filterEvents, name="filterEvents"),
      path("<int:event_id>/export_attendees_to_xlsx/", views.export_attendees_to_xlsx, name="export_attendees_to_xlsx"),
      
  ]