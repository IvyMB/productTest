from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from product.models import Product
from product.serializers import ProductSerializer, ProductDetailSerializer


class ProductCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

