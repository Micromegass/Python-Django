
from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request)
	print(request.user)
	#return HttpResponse("<h1> Hello World</h1>")  #string of HTML code
	return render(request, "home.html", {})


def about_view(request, *args, **kwargs):

	my_dic = {
		"mysentence" : "this is a sentence",
		"mynumber" : 123,
		"my_list" : [12213, "name", "21214", 899.0993]
	}

	return render(request, "about.html", my_dic )


def contact_view(request, *args, **kwargs):
	return  render(request, "contacting.html", {})


def social_view(request, *args, **kwargs):
	return render(request, "social.html", {})

