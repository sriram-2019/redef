from django.urls import path
from .views import qr_redirect

urlpatterns = [
    path("qr_redirect/", qr_redirect, name="qr_redirect"),
]
