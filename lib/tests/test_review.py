import unittest
from lib.customer import Customer
from lib.review import Review


class TestCustomer(unittest.TestCase):
    def test_add_review(self):
        customer = Customer("Alice", "Johnson")
        customer.add_review("Tasty Place", 8)
        self.assertEqual(len(Review.all()), 2)


if __name__ == '__main__':
    unittest.main()
