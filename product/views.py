from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
import logging
from product.models import Product
from product.serializers import ProductSerializer


logger = logging.getLogger(__name__)


class ProductCreateListView(generics.ListCreateAPIView):
    # Only get and options methods is allowed without authentication token
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            logger.info(f'User {request.user.username} create a new product with ID: {product.id}.')
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.info(f'User {request.user.username} has an bad request {serializer.errors}.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # Only get and options methods is allowed without authentication token
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def put(self, request, *args, **kwargs):
        identification = kwargs.get('pk', None)
        product = self.get_object()

        if product:
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()

                # Exemplo de logging
                logger.info(f'User {request.user.username} update the product {identification}.')
                return Response(serializer.data, status=status.HTTP_200_OK)

            logger.info(f'User {request.user.username} has an bad request {serializer.errors}.')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        identification = kwargs.get('pk', None)
        product = self.get_object()

        if product:
            product.delete()
            logger.info(f'User {request.user.username} delete the product {identification}.')
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
