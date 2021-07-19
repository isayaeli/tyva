from django.urls import path, re_path
from .views import CalendarView,event, add_event, edit_event

urlpatterns = [
    path('calendar/', CalendarView.as_view(), name='calendar'),
    # re_path(r'^event/new/$', event, name='event_new'),
    path('add_event/', add_event, name='event_new' ),
    # re_path(r'^event/edit/(?P<id>\d+)/$', edit_event, name='event_edit'),
    path('edit_event/<int:id>/', edit_event,  name="event_edit")
]
