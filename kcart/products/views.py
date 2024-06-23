from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def list_product(request):
    return render(request,'product.html')

def single_product(request):
    return render(request,'product_detail.html')

