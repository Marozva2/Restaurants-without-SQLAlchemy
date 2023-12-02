from review import Review


class Restaurant:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Restaurant name must be a string")
        self._name = name.strip()

    def name(self):
        return self._name

    def reviews(self):
        return [review for review in Review.all() if review.restaurant() == self._name]

    def customers(self):
        return set([review.customer() for review in self.reviews()])

    def average_star_rating(self):
        if not self.reviews():
            return 0
        total_rating = sum(review.rating() for review in self.reviews())
        average = total_rating / len(self.reviews())
        return average


restaurant1 = Restaurant("Sippin' Serenade")
print(restaurant1.name())
