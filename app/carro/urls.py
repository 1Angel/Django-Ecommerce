from django.urls import path

from carro.views import checkout

urlpatterns = [
    path('checkout/', checkout)
]