from django.db.models.base import Model
from django.forms import ModelForm, DateInput
from django import forms
from django.forms.widgets import DateTimeInput, TextInput, Textarea
from .models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'date','class':'form-control'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'date', 'class':'form-control'}, format='%Y-%m-%dT%H:%M'),
      'note': Textarea(attrs={'class':'form-control','rows':5}),
      'title': TextInput(attrs={'class':'form-control'}),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class addEventForm(forms.Form):
    title = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    note = forms.CharField(widget=Textarea(attrs={'class':'form-control','rows':5}))
    start_time = forms.DateTimeField(widget=DateTimeInput(attrs={'type':'date','class':'form-control'}))
    end_time = forms.DateTimeField(widget=DateTimeInput(attrs={'type':'date', 'class':'form-control'}))

    class Meta:
        model = Event
        fields = '__all__'


class editEventForm(forms.ModelForm):
    title = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    note = forms.CharField(widget=Textarea(attrs={'class':'form-control','rows':5}))
    start_time = forms.DateField(widget=DateInput(attrs={'type':'date','class':'form-control'}))
    end_time = forms.DateField(widget=DateInput(attrs={'type':'date', 'class':'form-control'}))

    class Meta:
        model = Event
        fields = '__all__'

