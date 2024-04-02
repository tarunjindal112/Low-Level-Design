import random
import string


class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand: str, catalogue_price: int, electric: bool):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02

        return self.catalogue_price * tax_percentage

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehicle:
    vehicle_id: str
    licence_plate: str
    info: VehicleInfo

    def __init__(self, vehicle_id: str, license_plate: str, info: VehicleInfo):
        self.vehicle_id = vehicle_id
        self.licence_plate = license_plate
        self.info = info

    def print(self):
        self.info.print()
        print(f"Id: {self.vehicle_id}")
        print(f"Licence Plate: {self.licence_plate}")


class VehicleRegistry:
    vehicle_info = {}

    def register_vehicle(self, brand, catalogue_price, electric):
        self.vehicle_info[brand] = VehicleInfo(brand, catalogue_price, electric)

    def __init__(self):
        self.register_vehicle("Tesla Model 3", 60000, True)
        self.register_vehicle("Volkswagen ID3", 35000, True)
        self.register_vehicle("BMW 5", 45000, False)

    def generate_vehicle_id(self, length):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase,k=2))}"

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:
    def register_vehicle(self, brand: string):
        registry = VehicleRegistry()

        return registry.create_vehicle(brand)


app = Application()
vehicle1 = app.register_vehicle("BMW 5")
vehicle1.print()
vehicle2 = app.register_vehicle("Tesla Model 3")
vehicle2.print()
vehicle3 = app.register_vehicle("Volkswagen ID3")
vehicle3.print()

