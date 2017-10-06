def odd_even(min,max):
    for i in range(min,max):
        if (i % 2) == 0:
            print "Number is", i, ". This is an even number."
        else :
            print "Number is", i, ". This is an odd number."

# odd_even(1,2000)

def multiply(list,multiplier):
    newlist = []
    for item in list:
        item *= multiplier
        newlist.append(item)

    return newlist

a = [2,4,10,16]
# print multiply(a,5)

def layered_multiples(arr):
    new_array = []
    for item in arr:
        holder = []
        for i in range(0,item):
            holder.append(1)
        new_array.append(holder)

    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
