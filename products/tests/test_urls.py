from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (
    all_products, product_detail, add_product, edit_product, delete_product
    )


# Testing urls for Products
class TestUrls(SimpleTestCase):

    def test_products_url_resolves(self):
        url = reverse('products')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_products)

    def test_product_add_url_resolves(self):
        url = reverse('add_product')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_product)

    def test_product_delete_url_resolves(self):
        url = reverse('delete_product', args=['product_id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, delete_product)
