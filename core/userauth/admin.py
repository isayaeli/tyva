from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profile
# Register your models here.
admin.site.unregister(Group)


# class ProfileAdmin(admin.ModelAdmin):
#     readonly_fields = ["slug",]
#     # search_fields = ["applied_by__username","applied_by__first_name","applied_by__last_name","employer","job"]


admin.site.register(Profile)