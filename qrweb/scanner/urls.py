from django.urls import path
from .views import qr_scanner, qr_redirect,create_qr,display_qr

urlpatterns = [
    path("", qr_scanner, name="qr_scanner"),
    path("redirect/", qr_redirect, name="qr_redirect"),
    path('create/', create_qr, name='create_qr'),
    path('display/', display_qr, name='display_qr'),
 
]
