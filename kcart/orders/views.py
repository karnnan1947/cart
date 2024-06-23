from django.shortcuts import render

# Create your views here.
def showcart(request):
    return render(request,'showcart.html')