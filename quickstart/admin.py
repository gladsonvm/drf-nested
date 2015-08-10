from django.contrib import admin
from quickstart.models import UserProfile, nestedmodel
# Register your models here.
admin.autodiscover()
admin.site.register(UserProfile)
admin.site.register(nestedmodel)
