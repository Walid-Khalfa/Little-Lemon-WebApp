from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_create_menu(self):
        menu = Menu.objects.create(
            title="Ice Cream", 
            price=80.00, 
            inventory=100
        )
        self.assertEqual(str(menu), "Ice Cream")
        self.assertEqual(menu.price, 80.00)
        self.assertEqual(menu.inventory, 100)

class BookingTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date="2024-02-25 18:00:00"
        )
        self.assertEqual(str(booking), "John Doe")