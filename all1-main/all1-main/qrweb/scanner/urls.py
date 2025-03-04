from django.urls import path
from .views import qr_scanner,create_qr

urlpatterns = [
    path("", qr_scanner, name="qr_scanner"),
   
    path('create/', create_qr, name='create_qr'),
   
]
