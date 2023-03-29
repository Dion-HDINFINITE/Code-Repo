class Car:

    def __init__(self, car_brand, car_plate_number, number_of_times_in_an_accident):
        self.car_brand = car_brand
        self.car_plate_number = car_plate_number
        self.number_of_times_in_an_accident = number_of_times_in_an_accident

    def get_descriptive(self):
        print(f"\nYour car brand is : {self.car_brand} \nPlate number is : {self.car_plate_number} "
              f"\nthe amount of times you have been in an accident : {self.number_of_times_in_an_accident}")


Lamborghini = Car("Lamborghini", "G 4 L 4 U", 3)
Rolls_Royce = Car("Rolls Royce", "R 4 ME", 1)
Tesla = Car("Tesla", "B 3 O L", 0)

Lamborghini.get_descriptive()
Rolls_Royce.get_descriptive()
Tesla.get_descriptive()