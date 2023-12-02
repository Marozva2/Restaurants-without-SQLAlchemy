from review import Review


class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._full_name = f"{given_name} {family_name}"
        Customer.customers.append(self)

    def set_given_name(self, given_name):
        if isinstance(given_name, str):
            self._given_name = given_name
            self._full_name = f"{given_name} {self._family_name}"

    def get_given_name(self):
        return self._given_name

    given_name = property(get_given_name, set_given_name)

    def set_family_name(self, family_name):
        if isinstance(family_name, str):
            self._family_name = family_name
            self._full_name = f"{self._given_name} {family_name}"

    def get_family_name(self):
        return self._family_name

    family_name = property(get_family_name, set_family_name)

    def full_name(self):
        return self._full_name

    @classmethod
    def all(cls):
        return cls.customers

    def __repr__(self):
        return f"{self._given_name} {self._family_name}"

    def restaurants(self):
        return list(set([review.restaurant() for review in Review.all() if review.customer() == self]))

    def add_review(self, restaurant, rating):
        Review(self.full_name(), restaurant, rating)

    def num_reviews(self):
        reviews = [review for review in Review.all(
        ) if review.customer() in self.full_name()]
        return len(reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.customers:
            if customer.full_name() == name:
                return customer
        else:
            print("customer not found")

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in Customer.all() if customer.given_name == name]


mycustomer = Customer("Frank", "Marozva")
newCustomer = Customer("John", "Smith")

mycustomer.add_review("orthega", 9)
print(Customer.find_by_name("John Smith"))

print(Customer.find_all_by_given_name("John"))
