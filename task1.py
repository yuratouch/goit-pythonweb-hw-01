from abc import abstractmethod, ABC


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = f"{spec} Spec"

    def __str__(self):
        return f"{self.make} {self.model} ({self.spec})"

    def start_engine(self):
        print(f"{self.make} {self.model} {self.spec}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = f"{spec} Spec"

    def __str__(self):
        return f"{self.make} {self.model} ({self.spec})"

    def start_engine(self):
        print(f"{self.make} {self.model} {self.spec}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def __init__(self):
        self.spec = "US"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.spec)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.spec)


class EUVehicleFactory(VehicleFactory):
    def __init__(self):
        self.spec = "EU"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.spec)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.spec)


# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

us_car = us_factory.create_car("Ford", "Mustang")
us_bike = us_factory.create_motorcycle("Harley-Davidson", "Iron 883")

eu_car = eu_factory.create_car("Volkswagen", "Passat")
eu_bike = eu_factory.create_motorcycle("Ducati", "Streetfighter V4")

us_car.start_engine()
us_bike.start_engine()
eu_car.start_engine()
eu_bike.start_engine()
