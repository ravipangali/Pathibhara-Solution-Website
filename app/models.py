from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class SiteSetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    hero_title = models.CharField(max_length=255, blank=True, null=True)
    hero_subtitle = models.CharField(max_length=255, blank=True, null=True)
    hero_image = models.ImageField(upload_to='hero/', null=True, blank=True)
    message = models.TextField(blank=True, null=True)
    whatsapp = models.CharField(max_length=500, blank=True, null=True)
    facebook = models.CharField(max_length=500, blank=True, null=True)
    instagram = models.CharField(max_length=500, blank=True, null=True)
    twitter = models.CharField(max_length=500, blank=True, null=True)
    linkedin = models.CharField(max_length=500, blank=True, null=True)
    youtube = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class About(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = CKEditor5Field(config_name='extends', blank=True, null=True)
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    mission = CKEditor5Field(config_name='extends', blank=True, null=True)
    vision = CKEditor5Field(config_name='extends', blank=True, null=True)
    objective = CKEditor5Field(config_name='extends', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OurTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='our_team/', null=True, blank=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = CKEditor5Field(config_name='extends', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services', blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    description = CKEditor5Field(config_name='extends', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
    
class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    description = CKEditor5Field(config_name='extends', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
    
class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    description = CKEditor5Field(config_name='extends', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    
class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='clients/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='testimonials')
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client.name

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name





