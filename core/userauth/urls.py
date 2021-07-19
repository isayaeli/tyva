from django.urls import path
from .views import login_request, logout_request, edit_profile

urlpatterns = [
    path('login/', login_request, name="login"),
    path('logout/',logout_request, name='logout'),
    path('edit_profile', edit_profile, name="edit_profile" )
]