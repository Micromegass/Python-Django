from django.shortcuts import render
from .forms import ProductForm
from .models import Product


def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		"form": form
	}
	return render(request, "product/product_create.html", context)


def product_detail_view(request):
	obj = Product.objects.get(id=1)

	# context = {
	# 	'title' : obj.title,
	# 	'description' : obj.description,
	# 	'price' : obj.price
	#
	# }

	context = {
		"object": obj
	}

	return render(request, "product/detail.html", context)
