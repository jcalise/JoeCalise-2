
me = {"name": "Joe", "age": 32, "country of birth": "USA", "favorite language": "Python"}

def printDict(dict):
    for key,item in dict.iteritems():
        print "My", key, "is", item

printDict(me)
