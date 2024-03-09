from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name= 'bho-home'),
    path('about/', views.about, name= 'bho-about')

]