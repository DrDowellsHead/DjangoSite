from django.contrib import admin
from .models import SliderPhoto


@admin.register(SliderPhoto)
class SliderPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
