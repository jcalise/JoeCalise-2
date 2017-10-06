import random

def cointoss(reps):
    tails = 0
    heads = 0
    for i in range(0,reps):
        rand = round(random.random())
        if rand == 0:
            tails += 1
            print "Attempt #", i + 1, ": throwing a coin...It's a tails! ... Got", heads, "heads so far and", tails, "tails so far."
        else:
            heads += 1
            print "Attempt #", i + 1, ": throwing a coin...It's a heads! ... Got", heads, "heads so far and", tails, "tails so far."

cointoss(5000)
