class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive", " ")

    def __str__(self):
        return f"Vinodh"


class car(vehicle):
    def __init__(self, direction="Right"):
        self.direction = direction
        self.brand="Tata"
        self.model = "2023"

    def turns(self):
        print("Car turns :", self.direction)

    def __str__(self):
        # return f"My Car Brand is {car1.brand} and model is {car1.model}"
        return "My Car Brand is {} and model is {}.".format(self.brand, self.model)


car1 = car()
print(car1, end=' ')
car1.move()
car1.turns()

print(car1)
