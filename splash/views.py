from django.shortcuts import render, redirect
from django.http import FileResponse
from django.conf import settings

from .models import Interest, Guestbook

import os


def index(request):
	try:
		interests = Interest.objects.all()
	except Interest.DoesNotExist:
		raise Http404('Interests does not exists')
	return render(request, 'splash/index.html', {'interests': interests})


def download_resume(request):
	file_path = os.path.join(settings.BASE_DIR, 'splash', 'static', 'splash', 'res-sum-2024.pdf')
	return FileResponse(open(file_path, 'rb'), content_type='application/pdf')


def contact(request):
	return render(request, 'splash/contact.html')
	

def guestbook(request):
	if request.method == 'GET':
		return render(request, 'splash/guestbook.html')

	name = request.POST.get('name')
	location = request.POST.get('location')
	comment = request.POST.get('comment')

	Guestbook.objects.create(name=name, location=location, comment=comment)
	return redirect('index')


def portfolio(request):
	return render(request, 'splash/portfolio.html')
	