class MathDojo(object):
    def __init__(self):
        self.value = 0

    def add(self, num1, *nums):
        self.value += num1
        for num in nums:
            self.value += num
        return self

    def subtract(self, num1, *nums):
        self.value -= num1
        for num in nums:
            self.value -= num
        return self

    def result(self):
        print self.value

md = MathDojo()

md.add(2).add(2,5).subtract(3,2).result()
#
# md.add([1]).result()
# md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
