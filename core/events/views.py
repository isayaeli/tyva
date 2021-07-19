# import calendar
# from datetime import date, datetime, timedelta,date
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import generic
# from django.utils.safestring import mark_safe

# from .models import *
# from events.utils import Calendar

# class CalendarView(generic.ListView):
#     model = Event
#     template_name = 'events/calendar.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # use today's date for the calendar
#         d = get_date(self.request.GET.get('day', None))

#         # Instantiate our calendar class with today's year and date
#         cal = Calendar(d.year, d.month)

#         # Call the formatmonth method, which returns our calendar as a table
#         html_cal = cal.formatmonth(withyear=True)
#         context['calendar'] = mark_safe(html_cal)
#         d = get_date(self.request.GET.get('month', None))
#         context['prev_month'] = prev_month(d)
#         context['next_month'] = next_month(d)
#         return context

# def get_date(req_day):
#     if req_day:
#         year, month = (int(x) for x in req_day.split('-'))
#         return date(year, month, day=1)
#     return datetime.today()


# def prev_month(d):
#     first = d.replace(day=1)
#     prev_month = first - timedelta(days=1)
#     month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
#     return month

# def next_month(d):
#     days_in_month = calendar.monthrange(d.year, d.month)[1]
#     last = d.replace(day=days_in_month)
#     next_month = last + timedelta(days=1)
#     month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
#     return month


from datetime import datetime, timedelta, date
from django.forms.widgets import RadioSelect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from django.views.generic.edit import UpdateView

from .models import *
from .utils import Calendar
from .forms import EventForm, addEventForm, editEventForm

# def index(request):
#     return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'events/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        events = Event.objects.all()
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['events'] = events
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    event = Event()
    print(request.POST)
    if request.POST and form.is_valid():
        # event.title = form.cleaned_data['title']
        # event.note = form.cleaned_data['note']
        # event.start_time = form.cleaned_data['start_time']
        # event.end_time = form.cleaned_data['end_time']
        form.save()
        return redirect('calendar')
    return render(request, 'events/event.html', {'form': form})

def add_event(request):
    if request.method == 'POST':
        form = addEventForm(request.POST or None)
        event = Event()
        if form.is_valid():
            event.title = form.cleaned_data['title']
            event.note = form.cleaned_data['note']
            event.start_time = form.cleaned_data['start_time']
            event.end_time = form.cleaned_data['end_time']
            event.save()
            return redirect('calendar')
    form = addEventForm()
    context = {
        'form':form
    }        
    return render(request, 'events/event.html', context)


def edit_event(request, id):
    event = Event.objects.get(id=id)
    if request.method == 'POST':
        print(request.POST)
        form = editEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        else:
            return redirect('home')
    else:
        form = editEventForm(instance=event)
    context = {
        'form':form,
        'event':event
    }
    return render(request, 'events/event.html',context)

  
