from django.urls import path
from .views import home, timeline

urlpatterns = [
    path('', home, name='home'),
    # path('email', email, name='email'),
    path('timeline/<str:slug>', timeline, name='timeline'),
]