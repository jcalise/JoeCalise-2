#Code that will print all of the odd numbers from 1 to 1000
for i in range(0,1000):
    if (i % 2) == 0: #checks if even or odd
        continue #if even skip
    else:
        print i #if odd print

#Code that will print the multiples of 5 up to 1,000,000
for i in range (5,1000000):
    if (i % 5) == 0: #checks if it's a multiple of 5
        print i #prints if true
    else:
        continue    #skips if not

'''
Alternative to the multiples:
#multiples A
for count in range(1, 1001, 2):
    print count

#multiples B
for count in range(5,1000001,5):
    print count'''

#printing the sum of a list
a = [1, 2, 5, 10, 255, 3]
print sum(a)

#determine the average of a list
print sum(a) / len(a) #sum of the list divided by the number of items in the list
