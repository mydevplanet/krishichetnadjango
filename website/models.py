from django.db import models

# Create your models here.

class Slide(models.Model):
    slide_image=models.ImageField(upload_to='slides')
    slide_title=models.CharField(max_length=30)
    slide_description=models.CharField(max_length=100, blank=True)
    slide_is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.slide_title
    
class About(models.Model):
    about_page=models.CharField(max_length=20)
    about_heading=models.CharField(max_length=100)
    about_image_1=models.ImageField(upload_to='about/')
    about_image_2=models.ImageField(upload_to='about/')
    about_image_3=models.ImageField(upload_to='about/')
    about_image_4=models.ImageField(upload_to='about/')


class Event(models.Model):
    event_image=models.ImageField(upload_to='events')
    event_name=models.CharField(max_length=100)
    event_des=models.CharField(max_length=200)
    event_is_active=models.BooleanField()

    def __str__(self):
        return self.event_name

class Feature(models.Model):
    featured_image=models.ImageField(upload_to='feature/')
    feature_name=models.CharField(max_length=200)
    feature_heading=models.CharField(max_length=200)
    feature_content=models.TextField()

    def __str__(self):
        return self.feature_name

class Product(models.Model):
    product_image=models.ImageField(upload_to='products')
    product_name=models.CharField(max_length=200)
    product_price=models.FloatField()
    product_short_description=models.CharField(max_length=500)
    product_description=models.TextField()

    def __str__(self):
        return self.product_name

class Feedback(models.Model):
    feedback_image=models.ImageField(upload_to='feedbacks')
    feedback_name=models.CharField(max_length=200)
    feedback_profession=models.CharField(max_length=500)
    feedback_description=models.TextField()

    def __str__(self):
        return self.feedback_name