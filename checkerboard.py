num_loops = 15
alt = 0

for i in range(0,num_loops):
    if alt == 0:
        print "* * * *"
        alt += 1
    else:
        print " * * * *"
        alt -= 1
