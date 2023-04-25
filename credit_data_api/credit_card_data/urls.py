from django.urls import path
from . import views

urlpatterns = [
    path('', views.getCreditCards),
    path('create', views.addCreditCard),
    path('read/<str:pk>', views.getCreditCard),
    path('update/<str:pk>', views.updateCreditCard),
    path('delete/<str:pk>', views.deleteCreditCard)
]