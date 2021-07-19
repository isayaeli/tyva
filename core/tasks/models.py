from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tinymce.models import HTMLField

# Create your models here.

PRIORITY = (
    ('label-success','high'),
    ('label-primary','medium'),
    ('label-danger','low')
)

TASK_STATUS  = (
    ('not_started','not-started'),
    ('started','started'),
    ('halfway_done','halfway-done' ),
    ('done', 'done')
)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(choices=PRIORITY,max_length=100)
    due_date =  models.DateTimeField(default=datetime.now)
    task_status = models.CharField(max_length=100, choices=TASK_STATUS, default='not_started')
    assigned_by = models.CharField(max_length=100, null=True, blank=True)
    task_todos =  HTMLField( null=True, blank=True)

    def __str__(self):
        return self.task_title
    
    # def get_absolute_url(self):
    #     return reverse_lazy('single_blog', kwargs={'id': self.blog_id})