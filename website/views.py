from django.shortcuts import render
from .models import Event, Partners, Feedback, Slide, About, Feature, Product
from .forms import InquiryForm
# Create your views here.

def home(request):
    slides=Slide.objects.all()
    abouts=About.objects.all()
    events=Event.objects.all()
    features=Feature.objects.all()
    products=Product.objects.all()
    feedbacks=Feedback.objects.all()
    partners=Partners.objects.all()
    context={
        'slides':slides,
        'abouts':abouts,
        'events':events,
        'features':features,
        'feedbacks':feedbacks,
        'products':products,
        'partners':partners,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'pages/about.html', {})


def product(request):
    return render(request, 'pages/products.html', {})


def store(request):
    return render(request, 'pages/store.html', {})

def contact(request):
    return render(request, 'pages/contact.html', {})

def feature(request):
    return render(request, 'pages/feature.html', {})

def article(request):
    return render(request, 'pages/article.html', {})

def testimonial(request):
    return render(request, 'pages/testimonial.html', {})

def inquiry_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = InquiryForm()

    return render(request, 'pages/contact.html', {'form': form})

