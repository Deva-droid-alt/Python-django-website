from django.urls import path
from AppCal import views

urlpatterns = [
    path('',views.indexpage_view,name='homepage'),
    path('calculate',views.calculate,name='calculate')
]