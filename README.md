**installation** 
---


    pip install django djangorestframework

**create folder**
---

    django-admin startproject Mypro
    

**Usage**

  + Mypro- settings.py installed-apps- insert : 
         ‘rest_framework’
  +  Mypro> 
         python manage.py startapp myapp
  +  Mypro> 
         python manage.py migrate     #create Database  #db.sqlite3
  +  Mypro>
         python manage.py runserver
   

+ Myapp> migrations>  views.py :
  
        from rest_framework.decorators import api_view
        from rest_framework.response import Response

        @api_view(["Get","post"])
        def say_hello(request):
        return Response({"message": "hello"})

+ Myapp> create new file > urls.py
       From Django.urls import path
       From myapp.views import say_hello

       Urlpatterns = [
       Path(“/hello”, say_hello)
      ]

+ Mypro> urls.py (base) :

  **Click import >**
      from django.contrib import admin
      from django.urls import path, include

      urlpatterns = [
      path("", include("myapp.urls")),
      path('admin/', admin.site.urls),

+ Mypro> settings.py
      INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'rest_framework',
      'myapp'

+ end:
      python manage.py runserver
