class Car:

	def __init__(self, make, model, year, color, new, manual):

		self.make = make
		self.model = model
		self.year = year
		self.color = color
		self.new = new
		self.manual = manual
		self.odometer = 0

	def get_descriptive(self):
		return f"This car is a {self.make}'s car.\nIts model is {self.model}-{self.year}.\nIt has {self.color} color."

	def increment_odometer(self, kms):
		self.odometer += kms
		print(f"The odometer has been updated to {self.odometer}kms.")

	def fill_gas_tank(self):
		print(f"The car is full of fuel right now!.")

	def change_color(self, new_color):
		self.color = new_color
		print(f"The color has been updated to {self.color}.")


class ElectricCar(Car):

	def __init__(self, make, model, year, color, new, manual):
		super().__init__(make, model, year, color, new, manual)
		self.battery = {"capacity": 100, "size": 5000}

	def fill_gas_tank(self):
		print("This car doesnt need gas you moron")

	def charge_battery(self):
		print("This car had been fully charged")


class Electricbus(ElectricCar):

	def __init__(self, make, model, year, color, new, manual):
		super().__init__(make, model, year, color, new, manual)
		self.battery = {"capacity": 350, "size": 13500}

	def shrink(self):
		print("Ok commencing shrinking in 3..2..1. ARE YOU AN IDIOT? THIS IS NOT THE MAGIC SCHOOL BUS!!!")

	def rave(self):
		print("Aw hell yea! its gonna get lit in here")


hyundai = ElectricCar("\thyundai", "kona ev", 2020, "black", True, False)
print(hyundai.get_descriptive())
hyundai.fill_gas_tank()
hyundai.charge_battery()

print()

volvo = Electricbus("volvo", 7900, 2018, "white", True, False)
print(volvo.get_descriptive())
volvo.shrink()
volvo.rave()
# toyota = Car("toyota", "yaris", 2020, "black", True, True)
# print(toyota.get_descriptive())
# toyota.increment_odometer(100)
# toyota.fill_gas_tank()
# toyota.change_color("blue")
