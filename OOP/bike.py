class bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "Price:", self.price, "Max Speed;", self.max_speed, "Total Miles:", self.miles
        return self

    def ride(self):
        print "Riding..."
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing..."
        self.miles -= 5
        return self


bike1 = bike(200,"25mph")
bike2 = bike(300,"35mph")
bike3 = bike(100,"15mph")

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()
