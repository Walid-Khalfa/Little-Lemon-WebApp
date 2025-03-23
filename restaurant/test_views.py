from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu1 = Menu.objects.create(title="Pizza", price=100.00, inventory=50)
        self.menu2 = Menu.objects.create(title="Burger", price=80.00, inventory=100)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)