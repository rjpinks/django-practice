from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os


def index(request):
	return render(request, 'splash/index.html')
	

def download_portfolio(request):
	file_path = os.path.join(settings.BASE_DIR, 'splash', 'static', 'splash', 'res-sum-2024.pdf')
	return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
