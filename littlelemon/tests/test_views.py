from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializers
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="Pizza", price=120, inventory=20)
        self.item2 = Menu.objects.create(title="Burger", price=80, inventory=30)

    def test_get_all(self):
        response = self.client.get(reverse('menu-list'))  # Use your actual URL name
        items = Menu.objects.all()
        serializer = MenuSerializers(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
