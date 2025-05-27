from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSetting, About, OurTeam, Category, Product, ProductImage,
    Service, Project, Blog, Client, Testimonial, Contact
)

# Inline classes for related models
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 1

# Custom Admin classes for each model
@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    search_fields = ['name', 'email']
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'email', 'phone', 'address')
        }),
        ('Media', {
            'fields': ('logo', 'hero_image')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle')
        }),
        ('Social Media', {
            'fields': ('facebook', 'instagram', 'twitter', 'linkedin', 'youtube')
        }),
        ('Other', {
            'fields': ('message',)
        }),
    )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    fieldsets = (
        (None, {
            'fields': ('title', 'image')
        }),
        ('Content', {
            'fields': ('description', 'mission', 'vision', 'objective')
        }),
    )

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'phone', 'email', 'image_tag']
    search_fields = ['name', 'designation', 'email']
    fieldsets = (
        (None, {
            'fields': ('name', 'designation', 'phone', 'email', 'image')
        }),
        ('Social Media', {
            'fields': ('facebook', 'instagram', 'twitter', 'linkedin', 'youtube')
        }),
    )
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None
    image_tag.short_description = 'Image'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'created_at']
    search_fields = ['name']
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None
    image_tag.short_description = 'Image'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'image_tag', 'created_at']
    search_fields = ['name']
    list_filter = ['category']
    list_editable = ['price']
    inlines = [ProductImageInline]
    ordering = ['name']
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None
    image_tag.short_description = 'Image'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_at']
    search_fields = ['name']
    list_filter = ['category']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'image_tag', 'created_at']
    search_fields = ['name']
    list_filter = ['category']
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None
    image_tag.short_description = 'Image'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None
    image_tag.short_description = 'Image'

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'created_at']
    search_fields = ['name']
    inlines = [TestimonialInline]
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None
    image_tag.short_description = 'Image'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client', 'message', 'created_at']
    search_fields = ['client__name', 'message']
    list_filter = ['client']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]
    def has_add_permission(self, request):
        return False