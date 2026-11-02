import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchByCategory(unittest.TestCase):
    def test_search_by_category_case_insensitive(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
        ]
        found = search_by_category(items, "animation")
        self.assertEqual([d.title for d in found], ["The Lion King"])
