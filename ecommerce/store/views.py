from django.shortcuts import render

from . models import Category,Product

def store(request):

    all_products = Product.objects.all()

    context = {'my_products': all_products}
    
    return render(request, 'store/store.html',context)


def categories(request):
    
    all_categories = Category.objects.all()

    return {'all_categories': all_categories}