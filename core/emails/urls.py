from django.urls import path
from .views import emails

urlpatterns = [
    path('email', emails, name="emails")
]