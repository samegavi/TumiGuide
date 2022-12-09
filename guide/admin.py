from django.contrib import admin

# Register your models here.
from .models import Place, Topic, Entry

admin.site.register(Place)
admin.site.register(Topic)
admin.site.register(Entry)
