import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestDiscount(unittest.TestCase):
    def test_discount_twenty_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=100.0))
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)

    def test_discount_invalid_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)
