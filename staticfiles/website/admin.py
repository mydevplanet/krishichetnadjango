from django.contrib import admin
from .models import Slide, About, Event
from django.db import models

class AboutAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        for field_name in obj._meta.get_fields():
            # Check if the field is an ImageField
            if isinstance(field_name, models.ImageField):
                # Get the existing instance
                existing_instance = About.objects.get(pk=obj.pk)
                # Compare the old image with the new one and delete the old image
                if getattr(existing_instance, field_name.name) != getattr(obj, field_name.name):
                    getattr(existing_instance, field_name.name).delete(save=False)

        obj.save()

# Register your models here.
admin.site.register(Slide)
admin.site.register(Event)
admin.site.register(About, AboutAdmin)