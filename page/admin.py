from django.contrib import admin
from .models import Parent, Child

admin.site.register(Parent)
admin.site.register(Child)
admin.site.site_header = 'My Admin'