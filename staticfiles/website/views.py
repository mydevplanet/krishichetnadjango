from django.shortcuts import render
from .models import Event, Slide, About
# Create your views here.

def home(request):
    slides=Slide.objects.all()
    abouts=About.objects.all()
    events=Event.objects.all()
    context={
        'slides':slides,
        'abouts':abouts,
        'events':events,
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'index.html', {})