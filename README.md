# Final Project

## Web Programming with Python and JavaScript
This Project is part of Harvard CS50W course provided by edx portal

## Objective
Building an Event Management System for any organization running conferences, workshops and renting Halls,
and registering coming attendees. This project is intended to be deployed in local networks as ERP.

## Description
This project contains:
* __Booking Page:__ This is the main page for booking and all requests are loaded in the same page without refresh using ajax, It displays all available Halls in a table with available time slots to book in green color. and if there are some slots occupied it will show them in red background color with event name displayed along in these cells, when user changed the date from Date changer section the display of time slot is changed automatically to display that date.
* __Create Event:__ This window will ask the employee(user) to enter the name of event, event details, Category and Organizer and if a certificate will be issued to attendees or not. Note this will not ask the user to enter a date or time, date and time will be in the next step.
* __Reserve time slots for the created event:__ Now user will select which hall to book and the desired free time slots in order to book them, then click "Reserve slots for selected date" button this will open an event list to choose from then click "Book Now!" you can repeat this action as much as you want and book as much dates with varing times and halls for the same event.
* __Page for each event:__ Now the just created event page will display event details, halls, dates, and time of start and finish and a form to add attendees.
* __Adding attendees:__ receptionist will greet attendees and register them and add their names, National IDs, email and mobile numbers.
* __removing attendees:__ also there is an option to remove attendee from that event or in other words unregister him from this event. 
* __Check if attendee exists and fetch info:__ just writing the National ID and leave this input field this will search the database and check if it is exists or not, if it is exist then fetch all data and auto complete the form and add him/her.
Note all these actions are using ajax in the same page without leaving it
* __Edit attendee details:__  click the National ID link will display a window to edit all attendee details.
* __Search attendees:__ search as you type by first or last name, National ID, email, mobile No. and display result in same page.
* __Export List of attendees/event as an Excel sheet:__ option to export List of attendees per event as .xlsx Microsoft Excel file using openpyxl library.
* __All attendees List:__ this page display all attendees and list of events he/she attended with links to these events and No. of Events being attended.
* __All Events List with Filter option:__ this page display all events sorted by date with an option to filter events by category.
* __Registration, Login, Logout:__ This is accomplished using the django built in user authentication system and crispy-form to enhance forms looking using bootstrap4 classes.
  
# Advantages for this system:
1. You can select as much halls for your event and select as much days and time slots. and all of that is displayed in a neat way.
2. clicking the just created event link will display a page of this event with all selected halls along with all dates and start and end times.
3. No overlapping events dates times or halls.


![Main Page](https://i.imgur.com/guy6vYL.jpg)

## Setup yours
 ```bash
 # clone repo via git then create virtual environment on windows
 $ py -m venv env

 # activating the virtual environment
 $ .\env\Scripts\activate

 # install all dependencies packages
 $ pip install -r requirements.txt

 # make migrations and start django server
 $ python manage.py migrate
 $ python manage.py runserver
 ```


## This Project by
[Magdi Nakhla](https://fb.me/nakhla)