from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse("Hello Home. This is trade")

def about_page(request):
    return HttpResponse("This is th about page")