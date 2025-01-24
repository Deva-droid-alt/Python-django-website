# urls.py
from django.contrib import admin
from django.urls import path
from TourApp import views  # Import views from the current directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Firstpg, name='Firstpg'),
    path('trivandrum', views.trivandrum, name='trivandrum'),
    path('kollam', views.kollam, name='kollam'),
    path('kottayam', views.kottayam, name='kottayam'),
    path('ekm', views.ekm, name='ekm'),
    path('thrissur', views.thrissur, name='thrissur'),
]
