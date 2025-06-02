from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify

# Create your models here.
class SiteSetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    map_url = models.TextField(blank=True, null=True)
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
    # SEO fields
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(max_length=160, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
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
    established_year = models.CharField(max_length=4, blank=True, null=True)
    # SEO fields
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(max_length=160, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
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
    bio = models.TextField(blank=True, null=True)
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
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = CKEditor5Field(config_name='extends', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    is_featured = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    # SEO fields
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(max_length=160, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
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
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    # SEO fields
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(max_length=160, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ServiceFeature(models.Model):
    id = models.BigAutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, null=True, help_text="FontAwesome icon class (e.g., fa-laptop-code)")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return f"{self.service.name} - {self.title}"

class ServiceProcess(models.Model):
    id = models.BigAutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='processes')
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Service Processes"
        
    def __str__(self):
        return f"{self.service.name} - {self.title}"
    
    
class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    description = CKEditor5Field(config_name='extends', blank=True, null=True)
    author = models.ForeignKey(OurTeam, on_delete=models.SET_NULL, null=True, blank=True, related_name='blogs')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='blogs')
    # SEO fields
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(max_length=160, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
    
class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='clients/', null=True, blank=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='testimonials')
    message = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=5, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client.name

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name


# New models for the dynamic content in templates

class Milestone(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.CharField(max_length=4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'year']

    def __str__(self):
        return f"{self.year} - {self.title}"


class Statistic(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    value = models.IntegerField()
    icon = models.CharField(max_length=50, help_text="FontAwesome icon class (e.g., fa-users)")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title}: {self.value}"


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class BlogTag(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('blog', 'tag')

    def __str__(self):
        return f"{self.blog.title} - {self.tag.name}"


class FAQ(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question


class BusinessHour(models.Model):
    id = models.BigAutoField(primary_key=True)
    day = models.CharField(max_length=20)
    opening_time = models.CharField(max_length=20, blank=True, null=True)
    closing_time = models.CharField(max_length=20, blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        if self.is_closed:
            return f"{self.day}: Closed"
        return f"{self.day}: {self.opening_time} - {self.closing_time}"


class Subsidiary(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    descriptions = CKEditor5Field(config_name='extends', blank=True, null=True)
    logo = models.ImageField(upload_to='subsidiaries/logos/', null=True, blank=True)
    banner = models.ImageField(upload_to='subsidiaries/banners/', null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    # SEO fields
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(max_length=160, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Subsidiaries"


class SubsidiaryProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    subsidiary = models.ForeignKey(Subsidiary, on_delete=models.CASCADE, related_name='subsidiary_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_subsidiaries')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subsidiary.name} - {self.product.name}"

    class Meta:
        unique_together = ('subsidiary', 'product')
        verbose_name_plural = "Subsidiary Products"





