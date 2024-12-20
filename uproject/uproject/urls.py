"""uproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('latest/',views.latest),
    path('toly/',views.toly),
    path('boly',views.boly),
    path('holy/',views.holy),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.logout),
    path('signup/',views.signup)

]
# from django.contrib import admin
# from django.urls import path,include
#
# from testapp import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("",views.my),
#     path('home/',views.home),
#     path('tollywood/',views.java),
#     path('bollywood/',views.python),
#     path('hollywood/',views.aplitude),
#     path('accounts/',include('django.contrib.auth.urls')),
#     path('logout/',views.logout),
#     path('signup/',views.signup)
# ]

