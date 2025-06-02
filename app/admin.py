from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSetting, About, OurTeam, Category, Product, ProductImage,
    Service, ServiceFeature, ServiceProcess, Blog, Client, Testimonial, Contact,
    Milestone, Statistic, Tag, BlogTag, FAQ, BusinessHour,
    Subsidiary, SubsidiaryProducts
)

# Inline classes for related models
class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1

class TestimonialInline(admin.StackedInline):
    model = Testimonial
    extra = 1

class ServiceFeatureInline(admin.StackedInline):
    model = ServiceFeature
    extra = 1

class ServiceProcessInline(admin.StackedInline):
    model = ServiceProcess
    extra = 1

class BlogTagInline(admin.StackedInline):
    model = BlogTag
    extra = 1

# Custom Admin classes for each model
@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    search_fields = ['name', 'email']
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'email', 'phone', 'address', 'map_url')
        }),
        ('Media', {
            'fields': ('logo', 'hero_image')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle')
        }),
        ('Social Media', {
            'fields': ('whatsapp', 'facebook', 'instagram', 'twitter', 'linkedin', 'youtube')
        }),
        ('Other', {
            'fields': ('message',)
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
    )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'established_year', 'created_at']
    search_fields = ['title']
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'established_year')
        }),
        ('Content', {
            'fields': ('description', 'mission', 'vision', 'objective')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
    )

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'phone', 'email', 'image_tag']
    search_fields = ['name', 'designation', 'email']
    fieldsets = (
        (None, {
            'fields': ('name', 'designation', 'phone', 'email', 'image', 'bio')
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
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'description', 'image', 'slug')
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None
    image_tag.short_description = 'Image'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'image_tag', 'is_featured', 'is_new', 'created_at']
    search_fields = ['name']
    list_filter = ['category', 'is_featured', 'is_new']
    list_editable = ['price', 'is_featured', 'is_new']
    inlines = [ProductImageInline]
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'price', 'image', 'slug')
        }),
        ('Status', {
            'fields': ('is_featured', 'is_new')
        }),
        ('Content', {
            'fields': ('description',)
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
    )
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
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ServiceFeatureInline, ServiceProcessInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'icon', 'slug')
        }),
        ('Content', {
            'fields': ('description',)
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'image_tag', 'created_at']
    search_fields = ['title', 'author__name', 'category__name']
    list_filter = ['created_at', 'author', 'category']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    inlines = [BlogTagInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'category', 'image', 'slug')
        }),
        ('Content', {
            'fields': ('description',)
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
    )
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None
    image_tag.short_description = 'Image'

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'website', 'image_tag', 'created_at']
    search_fields = ['name']
    inlines = [TestimonialInline]
    fields = ('name', 'image', 'designation', 'website')
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None
    image_tag.short_description = 'Image'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client', 'rating', 'created_at']
    search_fields = ['client__name', 'message']
    list_filter = ['client', 'rating']
    fields = ('client', 'message', 'rating')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]
    def has_add_permission(self, request):
        return False

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ['year', 'title', 'order', 'created_at']
    search_fields = ['year', 'title', 'description']
    list_filter = ['year']
    list_editable = ['order']
    ordering = ['order', 'year']
    fields = ('year', 'title', 'description', 'order')

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ['title', 'value', 'icon', 'order']
    search_fields = ['title']
    list_editable = ['value', 'order']
    ordering = ['order']
    fields = ('title', 'value', 'icon', 'order')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'order', 'is_active', 'created_at']
    search_fields = ['question', 'answer']
    list_filter = ['is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']
    fields = ('question', 'answer', 'order', 'is_active')

@admin.register(BusinessHour)
class BusinessHourAdmin(admin.ModelAdmin):
    list_display = ['day', 'opening_time', 'closing_time', 'is_closed', 'order']
    list_editable = ['opening_time', 'closing_time', 'is_closed', 'order']
    ordering = ['order']
    fields = ('day', 'opening_time', 'closing_time', 'is_closed', 'order')

# Subsidiary Products Inline
class SubsidiaryProductsInline(admin.StackedInline):
    model = SubsidiaryProducts
    extra = 1
    autocomplete_fields = ['product']

@admin.register(Subsidiary)
class SubsidiaryAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo_tag', 'banner_tag', 'product_count', 'created_at']
    search_fields = ['name', 'descriptions']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SubsidiaryProductsInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'slug')
        }),
        ('Media', {
            'fields': ('logo', 'banner')
        }),
        ('Content', {
            'fields': ('descriptions',)
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
    )
    
    def logo_tag(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 8px;" />', obj.logo.url)
        return None
    logo_tag.short_description = 'Logo'
    
    def banner_tag(self, obj):
        if obj.banner:
            return format_html('<img src="{}" width="80" height="40" style="object-fit: cover;" />', obj.banner.url)
        return None
    banner_tag.short_description = 'Banner'
    
    def product_count(self, obj):
        return obj.subsidiary_products.count()
    product_count.short_description = 'Products'

@admin.register(SubsidiaryProducts)
class SubsidiaryProductsAdmin(admin.ModelAdmin):
    list_display = ['subsidiary', 'product', 'created_at']
    search_fields = ['subsidiary__name', 'product__name']
    list_filter = ['subsidiary', 'product__category']
    autocomplete_fields = ['subsidiary', 'product']
    ordering = ['subsidiary', 'product']