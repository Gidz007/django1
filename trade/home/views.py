from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home_page(request):
    return HttpResponse("Hello Home. This is trade")

def about_page(request):
    return HttpResponse("This is th about page")

def contact_page(request):
    # This statement returns a render html document that has html code.
    return render(request, "contact.html")