"""
URL configuration for trade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
"""On this statement we import the home_page, about_page and the 
contact_page, and you can add as many as you a creating, we import
them from the home file undre views were our functions a. 
"""
from home.views import home_page, about_page, contact_page

"""if we leave the first quotes empty, this means this is our
      default page, if a person doesnt have a specific location.
    """,
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about/', about_page),
    path('contacts/', contact_page),
]
