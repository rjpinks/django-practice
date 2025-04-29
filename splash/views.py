from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings

from .models import Interest

import os


def index(request):
	interests = Interest.objects.all()
	return render(request, 'splash/index.html', {'interests': interests})
	

def download_resume(request):
	file_path = os.path.join(settings.BASE_DIR, 'splash', 'static', 'splash', 'res-sum-2024.pdf')
	return FileResponse(open(file_path, 'rb'), content_type='application/pdf')


def contact(request):
	return render(request, 'splash/contact.html', {'contacts': ['dummy data']})
	