from django.urls import path
from . import views

urlpatterns = [
    path('', views.getCreditCards),
    path('create', views.addCreditCards),
    path('read/<str:pk>', views.getCreditCards),
    path('update/<str:pk>', views.updateCreditCard),
    path('delete/<str:pk>', views.deleteCreditCard)

]