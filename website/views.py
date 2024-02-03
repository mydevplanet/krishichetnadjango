from django.shortcuts import render
from .models import Event, Feedback, Slide, About, Feature, Product
# Create your views here.

def home(request):
    slides=Slide.objects.all()
    abouts=About.objects.all()
    events=Event.objects.all()
    features=Feature.objects.all()
    products=Product.objects.all()
    feedbacks=Feedback.objects.all()
    context={
        'slides':slides,
        'abouts':abouts,
        'events':events,
        'features':features,
        'feedbacks':feedbacks,
        'products':products,
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'index.html', {})