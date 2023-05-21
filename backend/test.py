from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from cart.models import Category
from cart.models import Cart
from cart.models import CartItem
from cart.models import Article
from cart.serializers import CartSerializer


class CartListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('cart')
        self.cart_data = {'country': 'USA'}
        self.cart = Cart.objects.create(country='USA')

    def test_list_carts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.cart.id)
        self.assertEqual(response.data[0]['country'], self.cart.country)

    def test_create_cart(self):
        response = self.client.post(self.url, data=self.cart_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['country'], self.cart_data['country'])
        self.assertTrue(Cart.objects.filter(country=self.cart_data['country']).exists())

    def test_list_carts_with_filter(self):
        filtered_url = f"{self.url}?cart_id={self.cart.id}"
        response = self.client.get(filtered_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.cart.id)
        self.assertEqual(response.data[0]['country'], self.cart.country)


class ModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.cart = Cart.objects.create(country='Spain')
        self.article = Article.objects.create(name='Intel i5', price=2000, category=self.category)

    def test_category_str(self):
        category = Category.objects.get(name='Electronics')
        self.assertEqual(str(category), 'Electronics')

    def test_cart_str(self):
        cart = Cart.objects.get(country='Spain')
        self.assertIsNotNone(cart.created_at)
        self.assertEqual(str(cart), str(cart.created_at))

    def test_cart_total(self):
        cart_item = CartItem.objects.create(cart=self.cart, article=self.article, quantity=2)
        self.assertEqual(self.cart.total, 4000)

    def test_article_str(self):
        self.assertEqual(str(self.article), 'Intel i5')

    def tearDown(self):
        Category.objects.all().delete()
        Cart.objects.all().delete()
        Article.objects.all().delete()
        CartItem.objects.all().delete()