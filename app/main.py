class Car:

    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        if isinstance(comfort_class, int):
            if 1 <= comfort_class <= 7:
                self.comfort_class = comfort_class
        if isinstance(clean_mark, int):
            if 1 <= clean_mark <= 10:
                self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        if isinstance(distance_from_city_center, int):
            if 1.0 <= distance_from_city_center <= 10.0:
                self.distance_from_city_center = distance_from_city_center
        if isinstance(average_rating, float):
            if 1.0 <= average_rating <= 5.0:
                self.average_rating = average_rating
        self.clean_power = clean_power
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income_for_serv = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income_for_serv += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return income_for_serv

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center)
            , 1
        )

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        self.average_rating += 1
        if rate == 5:
            self.average_rating += 0.1
