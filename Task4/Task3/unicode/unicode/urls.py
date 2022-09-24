"""unicode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .import view
from search import views,view2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.home,name='home'),
    path('task3/',views.task3,name='task3'),
    path('top/',view2.top,name='top'),
    path('delete/',view2.delete,name='delete'),
]
