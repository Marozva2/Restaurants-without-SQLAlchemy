import unittest
from lib.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):
    def test_initialization(self):
        restaurant = Restaurant("Sippin Serenade")
        self.assertEqual(restaurant.name(), "Sippin Serenade")

    def test_reviews_method(self):
        restaurant = Restaurant("Delicious Diner")
        restaurant.reviews()

    def test_customers_method(self):
        restaurant = Restaurant("Cafe Supreme")
        restaurant.customers()

    def test_average_star_rating_method(self):
        restaurant = Restaurant("Tasty Tavern")
        restaurant.average_star_rating()


if __name__ == '__main__':
    unittest.main()
