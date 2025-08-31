# Base class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__engine_number = None  # Encapsulated attribute

    def set_engine_number(self, engine_number):
        self.__engine_number = engine_number

    def get_engine_number(self):
        return self.__engine_number

    def move(self):
        print(f"The {self.brand} {self.model} moves forward.")

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

# Subclass 1
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def move(self):
        print(f"The {self.brand} {self.model} drives smoothly on the road 🚗")

# Subclass 2
class Plane(Vehicle):
    def __init__(self, brand, model, year, wingspan):
        super().__init__(brand, model, year)
        self.wingspan = wingspan

    def move(self):
        print(f"The {self.brand} {self.model} soars through the skies ✈️")

# Subclass 3
class Boat(Vehicle):
    def __init__(self, brand, model, year, length):
        super().__init__(brand, model, year)
        self.length = length

    def move(self):
        print(f"The {self.brand} {self.model} sails gracefully across the water 🚤")

# Example usage
if __name__ == "__main__":
    # Assignment 1: Creating objects with unique values
    car1 = Car("Toyota", "Corolla", 2022, 4)
    car1.set_engine_number("ENG12345")
    car1.display_info()
    print("Engine Number:", car1.get_engine_number())
    car1.move()

    plane1 = Plane("Boeing", "747", 2018, "68m")
    plane1.set_engine_number("ENG98765")
    plane1.display_info()
    print("Engine Number:", plane1.get_engine_number())
    plane1.move()

    boat1 = Boat("Yamaha", "WaveRunner", 2021, "3m")
    boat1.set_engine_number("ENG55555")
    boat1.display_info()
    print("Engine Number:", boat1.get_engine_number())
    boat1.move()

    print("\n--- Polymorphism Demo ---")
    # Activity 2: Polymorphism in action
    vehicles = [car1, plane1, boat1]
    for v in vehicles:
        v.move()  # Same method name, different outputs
