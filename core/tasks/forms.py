from django import forms
from .models import Task



TASK_STATUS  = (
    ('not_started','not-started'),
    ('started','started'),
    ('halfway_done','halfway-done' ),
    ('done', 'done')
)

PRIORITY = (
    ('label-success','high'),
    ('label-primary','medium'),
    ('label-danger','low')
)


class taskForm(forms.ModelForm):
    task_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-round'}))
    priority = forms.ChoiceField(choices=PRIORITY, widget=forms.Select(attrs={'class':'form-control form-control-round'}))
    due_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'form-control form-control-round', 'type':'date'}))
    task_todos = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-round'}))
    
    

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('assigned_by', 'task_status')





class taskEditForm(forms.ModelForm):
    task_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-round'}))
    priority = forms.ChoiceField(choices=PRIORITY, widget=forms.Select(attrs={'class':'form-control form-control-round'}))
    due_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control form-control-round', 'type':'date'}))
    task_status = forms.ChoiceField( choices=TASK_STATUS, widget=forms.Select(attrs={'class':'form-control form-control-round'}))
    task_todos = forms.CharField(widget=forms.Textarea(attrs={'id':'dark'}))

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('user','assigned_by')



class assignTaskForm(forms.ModelForm):
    task_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-round'}))
    priority = forms.ChoiceField(choices=PRIORITY, widget=forms.Select(attrs={'class':'form-control form-control-round'}))
    due_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'form-control form-control-round', 'type':'date'}))
    task_todos = forms.CharField(widget=forms.Textarea(attrs={'id':'dark'}))
    

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('assigned_by', 'task_status')