from django.contrib import admin
from .models import Slide, About, Event, Feature, Product, Feedback, Partners
from django.db import models

# class AboutAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         try:
#         # Get all fields in the model
#             for field in obj._meta.get_fields():
#                 # Check if the field is an ImageField
#                 if isinstance(field, models.ImageField):
#                     # Get the existing instance
#                     existing_instance = About.objects.get(pk=obj.pk)
                    
#                     # Compare the old image with the new one
#                     old_image = getattr(existing_instance, field.name)
#                     new_image = getattr(obj, field.name)

#                     # Delete the old image if it has changed
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             raise

# Register your models here.
admin.site.register(Slide)
admin.site.register(Event)
admin.site.register(About)
admin.site.register(Feature)
admin.site.register(Feedback)
admin.site.register(Product)
admin.site.register(Partners)