from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('home/', views.home, name='home'),
    path('account/details/', views.account_details, name='account_details'),
    path('account/status/', views.account_status, name='account_status'),
    path('account/payments/', views.payments, name='payments'),
    path('account/bills/', views.bills, name='bills'),
    path('account/units/', views.units, name='units'),
     path('account/units/refute', views.units_refute, name='units_refute'),
]