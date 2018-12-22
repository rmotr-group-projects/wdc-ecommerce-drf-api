import json
from copy import deepcopy
from freezegun import freeze_time

from django.test import TestCase

from products.models import Product, Category


class ProductTestCase(TestCase):

    @freeze_time('2018-12-20T10:15:30+00:00')
    def setUp(self):
        self.category_1 = Category.objects.create(name='Sport')
        self.category_2 = Category.objects.create(name='Clothes')

        self.product_1 = Product.objects.create(
            name='Nike Vapor',
            sku='44444444',
            category=self.category_1,
            description='Some product description',
            price=129.99)
        self.product_2 = Product.objects.create(
            name='Sweater',
            sku='88888888',
            category=self.category_2,
            description='Some product description',
            price=59.99)

    @freeze_time('2018-12-20T10:15:30+00:00')
    def test_detail(self):
        expected = {
            'id': self.product_1.id,
            'name': self.product_1.name,
            'sku': self.product_1.sku,
            'category': self.product_1.category.id,
            'description': self.product_1.description,
            'price': str(self.product_1.price),
            'created': '2018-12-20T10:15:30Z',
            'featured': self.product_1.featured
        }
        response = self.client.get('/api/products/{}/'.format(self.product_1.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(), expected)

    @freeze_time('2018-12-20T10:15:30+00:00')
    def test_list(self):
        expected = [
            {
                'id': self.product_1.id,
                'name': self.product_1.name,
                'sku': self.product_1.sku,
                'category': self.product_1.category.id,
                'description': self.product_1.description,
                'price': str(self.product_1.price),
                'created': '2018-12-20T10:15:30Z',
                'featured': self.product_1.featured
            },
            {
                'id': self.product_2.id,
                'name': self.product_2.name,
                'sku': self.product_2.sku,
                'category': self.product_2.category.id,
                'description': self.product_2.description,
                'price': str(self.product_2.price),
                'created': '2018-12-20T10:15:30Z',
                'featured': self.product_2.featured
            }
        ]
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(), expected)

    @freeze_time('2018-04-14T10:15:30+00:00')
    def test_create(self):
        self.assertEqual(Product.objects.count(), 2)
        payload = {
            'name': 'New product',
            'category': self.category_1.id,
            'sku': '11111111',
            'description': 'New product description',
            'price': 39.99
        }

        response = self.client.post(
            '/api/products/', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(Product.objects.count(), 3)

        product = Product.objects.get(name='New product')
        self.assertEqual(product.name, 'New product')
        self.assertEqual(product.category, self.category_1)
        self.assertEqual(product.sku, '11111111')
        self.assertEqual(product.description, 'New product description')
        self.assertEqual(float(product.price), 39.99)

    @freeze_time('2018-04-14T10:15:30+00:00')
    def test_full_update(self):
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(self.product_1.name, 'Nike Vapor')
        self.assertEqual(self.product_1.sku, '44444444')
        self.assertEqual(self.product_1.category, self.category_1)
        self.assertEqual(self.product_1.description, 'Some product description')
        self.assertEqual(self.product_1.price, 129.99)
        self.assertEqual(self.product_1.featured, False)

        payload = {
            'name': 'Updated name',
            'category': self.category_2.id,
            'sku': '11111111',
            'description': 'New product description',
            'price': 39.99,
            'featured': True
        }

        response = self.client.put(
            '/api/products/{}/'.format(self.product_1.id),
            data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(Product.objects.count(), 2)

        product = Product.objects.get(id=self.product_1.id)
        self.assertEqual(product.name, 'Updated name')
        self.assertEqual(product.sku, '11111111')
        self.assertEqual(product.category, self.category_2)
        self.assertEqual(product.description, 'New product description')
        self.assertEqual(float(product.price), 39.99)
        self.assertEqual(product.featured, True)

    @freeze_time('2018-04-14T10:15:30+00:00')
    def test_partial_update(self):
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(self.product_1.name, 'Nike Vapor')

        payload = {
            'name': 'Updated name',
        }

        response = self.client.patch(
            '/api/products/{}/'.format(self.product_1.id),
            data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(Product.objects.count(), 2)

        product = Product.objects.get(id=self.product_1.id)
        self.assertEqual(product.name, 'Updated name')

    @freeze_time('2018-04-14T10:15:30+00:00')
    def test_delete(self):
        self.assertEqual(Product.objects.count(), 2)

        response = self.client.delete(
            '/api/products/{}/'.format(self.product_1.id))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 1)
