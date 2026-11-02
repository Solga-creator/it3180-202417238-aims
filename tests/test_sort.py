import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestSortCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
        self.cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))
        self.cart.add_dvd(DigitalVideoDisc("The Lion King", cost=19.95))

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        self.assertEqual([d.title for d in self.cart.items], ["Aladdin", "Star Wars", "The Lion King"])

    def test_sort_by_cost_ascending(self):
        self.cart.sort_by_cost()
        self.assertEqual([d.title for d in self.cart.items], ["Aladdin", "The Lion King", "Star Wars"])

    def test_sort_by_cost_descending(self):
        self.cart.sort_by_cost(descending=True)
        self.assertEqual([d.title for d in self.cart.items], ["Star Wars", "The Lion King", "Aladdin"])
