import unittest

from aims.cart import MAX_NUMBERS_ORDERED, Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=1.0)))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("overflow", cost=1.0)))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_remove_missing_dvd(self):
        cart = Cart()
        missing = DigitalVideoDisc("Missing", cost=1.0)
        self.assertFalse(cart.remove_dvd(missing))
