class Car:
    def move(self): print("Car moving")
class Bike:
    def move(self): print("Bike moving")

for v in (Car(), Bike()): v.move()
