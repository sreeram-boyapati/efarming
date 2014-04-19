from django.contrib import admin
from .models import Crop

class CropAdmin(admin.ModelAdmin):
	list_display = ['name', 'type_crop', 'price', 'owner']
	search_fields = ['name', 'type_crop', 'owner']

admin.site.register(Crop, CropAdmin)