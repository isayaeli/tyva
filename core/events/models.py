from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)
    note = models.TextField(max_length=200)
    created_on = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.title
    

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<div class="bg-info rounded-pill text-center mt-1" ><a style="font-weight:bolder; color:white;" data-toggle="modal" data-target="#staticBackdrop2{self.id}" > {self.title} </a></div>'

    


