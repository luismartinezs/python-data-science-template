class Vehicle:
    def __init__(self, brand: str, speed: int):
        self.brand = brand
        self.speed = speed

    def display_details(self):
        print(f"Brand: {self.brand}, Speed: {self.speed}")


class Car(Vehicle):
    def __init__(self, brand: str, speed: int, num_doors: int):
        super().__init__(brand, speed)
        self.num_doors = num_doors

    def display_details(self):
        print(
            f"Brand: {self.brand}, Speed: {self.speed}, Number of doors: {self.num_doors}"
        )


vehicle = Vehicle("Toyota", 100)
vehicle.display_details()

car = Car("Toyota", 100, 4)
car.display_details()
