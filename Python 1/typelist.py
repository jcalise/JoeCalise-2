string = ""
number = 0

# l = ['magical unicorns',19,'hello',98.98,'world']
l = [2,3,1,7,4,12]
# l = ['magical','unicorns']

for i in l:
    if isinstance(i, int):
        number += i
    elif isinstance(i, str):
        string += i + " "
    elif isinstance(i, float):
        number += i
    else:
        print "What do you think I am?!?"

if all(isinstance(l, str) for l in l):
    print "This list you entered is of string type"
    print "String:", string
elif all(isinstance(l, int) for l in l):
    print "This list you entered is of integer type"
    print "Sum:", number
else:
    print "This list you entered is of mixed type"
    print "String:", string
    print "Sum:", number
