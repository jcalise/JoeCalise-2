class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price >= 10000:
            self.tax_rate = .15
        else:
            self.tax_rate = .12

        self.display_all()

    def display_all(self):
        print "Price:", self.price, "\nSpeed:", self.speed, "\nFuel:", self.fuel, "\nMileage:", self.mileage, "\nTax:", self.tax_rate

car1 = (2000, "35mph", "Full", "15mpg")
car2 = (2000, "5mph", "Not Full", "105mpg")
car3 = (2000, "15mph", "Kind of Full", "95mpg")
car4 = (2000, "25mph", "Full", "25mpg")
car5 = (2000, "45mph", "Empty", "25mpg")
car6 = (200000, "35mph", "Empty", "15mpg")
