from django.contrib import admin
from django.urls import path, include
from productos.API.views import ProductoCreate, ProductoList, ProductoDetail

urlpatterns = [
    path('create/', ProductoCreate.as_view(), name="productos-create"),
    path('list/', ProductoList.as_view(), name="productos-list"),
    path('list/<int:pk>', ProductoDetail.as_view(), name="producto-detail")
]