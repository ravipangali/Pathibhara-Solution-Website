from django.shortcuts import render
from app.models import (About, Blog, Category, Client, OurTeam, Product, ProductImage, Project, ProjectImage,
    Service, ServiceFeature, ServiceProcess, SiteSetting, Testimonial, Milestone, Statistic, Tag, FAQ, BusinessHour)
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings

# Create your views here.
def home(request):
    data = {
        'site_settings': SiteSetting.objects.first(),
        'services': Service.objects.all(),
        'about': About.objects.first(),
        'projects': Project.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'team': OurTeam.objects.all(),
        'clients': Client.objects.all(),
        'blogs': Blog.objects.all(),
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
        'stats': Statistic.objects.all()[:4],  # Get top 4 stats for homepage
        'featured_products': Product.objects.filter(is_featured=True)[:4],
    }
    return render(request, 'frontend/home.html', data)

def about(request):
    """About page view"""
    context = {
        'title': 'About Us',
        'about': About.objects.first(),
        'team_members': OurTeam.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'site_settings': SiteSetting.objects.first(),
        'milestones': Milestone.objects.all(),
        'stats': Statistic.objects.all(),
    }
    return render(request, 'frontend/about.html', context)

def services(request):
    """Services page view"""
    context = {
        'title': 'Our Services',
        'services': Service.objects.all(),
        'faqs': FAQ.objects.all(),
        'categories': Category.objects.all(),
        'site_settings': SiteSetting.objects.first(),
    }
    return render(request, 'frontend/services.html', context)

def service_detail(request, slug):
    """Service detail page view"""
    service = get_object_or_404(Service, slug=slug)
    related_services = Service.objects.exclude(id=service.id)[:3]
    
    context = {
        'testimonials': Testimonial.objects.all(),
        'title': service.name,
        'meta_title': service.meta_title or service.name,
        'meta_description': service.meta_description or service.description[:160] if service.description else '',
        'meta_keywords': service.meta_keywords,
        'service': service,
        'service_features': service.features.all(),
        'service_processes': service.processes.all(),
        'related_services': related_services,
        'site_settings': SiteSetting.objects.first(),
    }
    return render(request, 'frontend/service_detail.html', context)

def products(request):
    """Products page view"""
    context = {
        'title': 'Our Products',
        'products': Product.objects.all(),
        'categories': Category.objects.all(),
        'site_settings': SiteSetting.objects.first(),
        'featured_products': Product.objects.filter(is_featured=True),
        'new_products': Product.objects.filter(is_new=True),
    }
    return render(request, 'frontend/products.html', context)

def product_detail(request, slug):
    """Product detail page view"""
    product = get_object_or_404(Product, slug=slug)
    product_images = product.images.all() if hasattr(product, 'images') else []
    related_products = Product.objects.exclude(id=product.id)[:3]
    
    context = {
        'title': product.name,
        'meta_title': product.meta_title or product.name,
        'meta_description': product.meta_description or product.description[:160] if product.description else '',
        'meta_keywords': product.meta_keywords,
        'product': product,
        'product_images': product_images,
        'related_products': related_products,
        'site_settings': SiteSetting.objects.first(),
        'is_featured': product.is_featured,
        'is_new': product.is_new,
    }
    return render(request, 'frontend/product_detail.html', context)

def projects(request):
    """Projects page view"""
    context = {
        'title': 'Our Projects',
        'testimonials': Testimonial.objects.all(),
        'projects': Project.objects.all(),
        'categories': Category.objects.all(),
        'stats': Statistic.objects.all(),
        'site_settings': SiteSetting.objects.first(),
    }
    return render(request, 'frontend/projects.html', context)

def project_detail(request, slug):
    """Project detail page view"""
    project = get_object_or_404(Project, slug=slug)
    project_images = project.images.all() if hasattr(project, 'images') else []
    related_projects = Project.objects.exclude(id=project.id)[:3]
    
    context = {
        'title': project.name,
        'meta_title': project.meta_title or project.name,
        'meta_description': project.meta_description or project.description[:160] if project.description else '',
        'meta_keywords': project.meta_keywords,
        'project': project,
        'project_images': project_images,
        'related_projects': related_projects,
        'site_settings': SiteSetting.objects.first(),
    }
    return render(request, 'frontend/project_detail.html', context)

def blog(request):
    """Blog page view"""
    blogs = Blog.objects.all().order_by('-created_at')
    featured_post = blogs.first()
    
    context = {
        'title': 'Our Blog',
        'meta_description': 'Read the latest news, tips, and insights on our blog.',
        'posts': blogs,
        'featured_post': featured_post,
        'categories': Category.objects.all(),
        'recent_posts': blogs[:3],
        'site_settings': SiteSetting.objects.first(),
        'tags': Tag.objects.all(),
    }
    return render(request, 'frontend/blog.html', context)

def blog_detail(request, slug):
    """Blog detail page view"""
    post = get_object_or_404(Blog, slug=slug)
    recent_posts = Blog.objects.exclude(id=post.id).order_by('-created_at')[:3]
    related_posts = Blog.objects.exclude(id=post.id)[:2]
    
    context = {
        'title': post.title,
        'meta_title': post.meta_title or post.title,
        'meta_description': post.meta_description or post.description[:160] if post.description else '',
        'meta_keywords': post.meta_keywords,
        'post': post,
        'recent_posts': recent_posts,
        'related_posts': related_posts,
        'categories': Category.objects.all(),
        'site_settings': SiteSetting.objects.first(),
        'tags': Tag.objects.all(),
        'post_tags': post.tags.all(),
    }
    return render(request, 'frontend/blog_detail.html', context)

def contact(request):
    """Contact page view with form handling"""
    site_settings = SiteSetting.objects.first()
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        # Basic validation
        if name and email and message:
            # Send email (configure EMAIL settings in settings.py)
            try:
                send_mail(
                    f'Contact Form: {subject}',
                    f'From: {name} <{email}>\n\n{message}',
                    email,  # From email
                    [settings.DEFAULT_FROM_EMAIL],  # To email
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully. We will contact you soon!')
                return redirect('contact')
            except Exception as e:
                messages.error(request, f'There was an error sending your message. Please try again later.')
        else:
            messages.error(request, 'Please fill all required fields.')
    
    context = {
        'title': 'Contact Us',
        'meta_title': 'Contact Us | Get in Touch with Our Team',
        'meta_description': 'Contact us today to discuss your project requirements or any questions you have about our services.',
        'company_address': site_settings.address if site_settings else None,
        'company_email': site_settings.email if site_settings else None,
        'company_phone': site_settings.phone if site_settings else None,
        'site_settings': site_settings,
        'faqs': FAQ.objects.filter(is_active=True),
        'business_hours': BusinessHour.objects.all(),
    }
    return render(request, 'frontend/contact.html', context)