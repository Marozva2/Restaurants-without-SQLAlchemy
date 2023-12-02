import unittest
from lib.customer import Customer


class TestCustomer(unittest.TestCase):
    def test_initialization(self):
        customer = Customer("John", "Doe")
        self.assertEqual(customer.given_name, "John")
        self.assertEqual(customer.family_name, "Doe")

    def test_full_name(self):
        customer = Customer("Jane", "Smith")
        self.assertEqual(customer.full_name(), "Jane Smith")

    def test_add_review(self):
        customer = Customer("Alice", "Johnson")
        customer.add_review("Tasty Place", 8)
        # self.assertEqual(len(customer.restaurants()), 1)
        # self.assertEqual(customer.restaurants()[1].name(), "Tasty Place")

    def test_num_reviews(self):
        customer = Customer("Bob", "Williams")
        customer.add_review("Cozy Cafe", 7)
        customer.add_review("Gourmet Grill", 9)
        self.assertEqual(customer.num_reviews(), 2)

    def test_find_by_name(self):
        customer = Customer("Alex", "Brown")
        self.assertEqual(Customer.find_by_name("Alex Brown"), customer)

    def test_find_all_by_given_name(self):
        Customer("Chris", "Miller")
        Customer("Chris", "Jones")
        customers = Customer.find_all_by_given_name("Chris")
        self.assertEqual(len(customers), 2)


if __name__ == '__main__':
    unittest.main()
