

import datetime

class Car:
    total_car_built: int = 0
    def __init__(self, name: str, model: datetime):
        self.name: str = name
        self.model: datetime = model
        Car.total_car_built += 1

    @classmethod
    def get_total_cars(cls, cars: list):
        return f"\nTotal cars built: {cls.total_car_built} and the cars are: {', '.join([car.name for car in cars])}\n"

honda = Car("Honda", datetime.datetime(2020, 5, 17))
lambo = Car("Lamborghini", datetime.datetime(2021, 3, 10))
Civic = Car("Civic", datetime.datetime(2019, 8, 25))

print(Car.get_total_cars([honda, lambo, Civic]))