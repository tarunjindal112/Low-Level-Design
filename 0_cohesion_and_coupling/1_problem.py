import random
import string


class VehicleRegistry:
    def generate_vehicle_id(self, length):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase,k=2))}"


class Application:
    def register_vehicle(self, brand: string):
        registry = VehicleRegistry()
        vehicle_id = registry.generate_vehicle_id(12)
        license_plate = registry.generate_vehicle_license(vehicle_id)

        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        payable_tax = catalogue_price * tax_percentage

        print("Registration Complete. Vehicle Information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License Plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")


app = Application()
app.register_vehicle("BMW 5")
app.register_vehicle("Tesla Model 3")
app.register_vehicle("Volkswagen ID3")

