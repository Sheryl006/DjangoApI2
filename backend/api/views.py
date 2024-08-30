from django.shortcuts import render
from .models import Product,Car,YourModel

from .serializers import ProductSerializer,CarSerializer,YourModelSerializer
from rest_framework import viewsets,filters

# class based view
# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']  # Fields you want to search


