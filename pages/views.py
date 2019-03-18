
from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request)
	print(request.user)
	#return HttpResponse("<h1> Hello World</h1>")  #string of HTML code
	return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})


def contact_view(request, *args, **kwargs):
	return  render(request, "contacting.html", {})


def social_view(request, *args, **kwargs):
	return render(request, "social.html", {})

