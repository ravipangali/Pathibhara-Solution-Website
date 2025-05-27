from django.shortcuts import render
from app.models import (About, Blog, Category, Client, OurTeam, Product, Project, Service,
    SiteSetting, Testimonial)

# Create your views here.
def home(request):
    data = {
        'site_settings': SiteSetting.objects.first(),
        'services': Service.objects.all(),
        'about': About.objects.first(),
        'projects': Project.objects.all(),
        'testimonials': Testimonial.objects.all(),
        # 'team': OurTeam.objects.all(),
        'clients': Client.objects.all(),
        'blogs': Blog.objects.all(),
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'frontend/home.html', data)
