from django.contrib import admin
from django.urls import path
from payment import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paymenthandler/', views.payment_callback, name='paymenthandler'),
    path('success/', views.payment_success, name='success'),
]