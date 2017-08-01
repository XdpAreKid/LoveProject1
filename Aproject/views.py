from django.shortcuts import render

# Create your views here.

def home(request):
    image = 'static/images/cover_bg_1.jpg'
    return render(request, 'index.html')

def whenwhere(request):
    return render(request, 'when-where.html')

def guest(request):
    return render(request,'guest.html')

def groom_bridge(request):
    return render(request, 'groom-bride.html')

def blog(request):
    return render(request, 'blog.html')

def gallery(request):
    return render(request, 'gallery.html')