from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.getCustomers),
    path('add/', views.addCustomer)
]