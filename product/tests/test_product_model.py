from django.test import TestCase
from product.models import Product


class ProductModelTest(TestCase):

    def test_create_product(self):
        product = Product.objects.create(name='Produto Teste', price=10.0)
        self.assertEqual(product.name, 'Produto Teste')
        self.assertEqual(product.price, 10.0)
