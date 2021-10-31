from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("generate_qr/", views.generate_qr),
    path("receive_xml/", views.receive_xml),
]
