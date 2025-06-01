from django.urls import path
from . import views

urlpatterns = [
    path('ckeditor/upload/', views.custom_upload_function, name='ckeditor_upload'),
]
