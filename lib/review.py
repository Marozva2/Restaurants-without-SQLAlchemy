class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating=None):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = None
        Review.reviews.append(self)

        if rating is not None:
            self.set_rating(rating)

    def set_rating(self, rating):
        if isinstance(rating, (int, float)):
            self._rating = rating

        else:
            print("Rating must be a number")

    def get_rating(self):
        return self._rating

    rating = property(get_rating, set_rating)

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    @classmethod
    def all(cls):
        return cls.reviews

    def __repr__(self):
        return f"{self._customer} ,{self._restaurant} {self._rating}"


myreview = Review("Frank", "Sippin serenade", 15)
newreview = Review("Marozva", "Del Ruiz", 14)

print(myreview.rating)
print(newreview.rating)

print(myreview.customer())
print(newreview.customer())

print(myreview.restaurant())
print(newreview.restaurant())

print(myreview)
print(newreview)
