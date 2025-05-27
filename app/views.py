from django.shortcuts import render
import uuid
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

# Create your views here.
@csrf_exempt
def custom_upload_function(request):
    """
    Handles CKEditor 5 file uploads and returns a JSON response with the file URL.
    """
    if request.method == "POST" and request.FILES.get("upload"):
        uploaded_file = request.FILES["upload"]

        # Generate a unique filename using UUID
        filename = f"{uuid.uuid4().hex}_{uploaded_file.name}"

        # Define the upload path
        upload_path = os.path.join("uploads", "ckeditor", filename)

        # Save the file using Django's default storage
        saved_path = default_storage.save(upload_path, ContentFile(uploaded_file.read()))

        # Generate the file URL
        file_url = settings.MEDIA_URL + saved_path

        # CKEditor 5 expects {"url": "file_url"} as a response
        return JsonResponse({"url": file_url})

    return JsonResponse({"error": "Invalid request"}, status=400)

