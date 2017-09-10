words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
newwords = words.replace('day', 'month', 1)
print newwords

x = [2,54,-2,7,12,98]
print "Min value is", min(x), ". Max value is", max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
last = len(y) - 1
print "First value:", y[0], "Last Value:", y[last]
newlist = [y[0], y[last]]
print newlist

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
length = len(x)
newlist = x[0:5]
longlist = newlist + x[6:length]
print longlist
