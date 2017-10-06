class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"

    def Sell(self):
        self.status = "Sold"
        return self

    def Tax(self, tax_rate):
        self.cost = self.price + (self.price * tax_rate)
        print self.cost
        return self

    def DisplayInfo(self):
        print "Price:", self.price
        print "Item Name:", self.item_name
        print "Price:", self.weight
        print "Price:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        return self

    def Return(self, return_reason):
        if return_reason == "Defective":
            self.status = "Defective"
            self.price = 0
            self.cost = 0
        elif return_reason == "Like New":
            self.status = "For Sale"
        elif return_reason == "Used":
            self.status = "Used"
            self.cost = self.price * .80
        else:
            print "Valid return reasons are Defective, Like New, Used."
        return self

prod1 = Product(100, "Stick", 1, "Nature", 100)

prod1.DisplayInfo().Return("Defective").DisplayInfo()
