from rest_framework import generics
from productos.API.serializers import ProductoSerializer
from productos.models import productos
from rest_framework import permissions
from rest_framework import filters
class ProductoCreate(generics.CreateAPIView):
    queryset = productos.objects.all()
    serializer_class = ProductoSerializer

class ProductoList(generics.ListAPIView):
    queryset = productos.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class ProductoDetail(generics.RetrieveAPIView):
    queryset = productos.objects.all()
    serializer_class = ProductoSerializer

