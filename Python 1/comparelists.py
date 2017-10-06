# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]
#
# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]
#
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

if (len(list_one) == len(list_two)):
    result = "The lists are the same."
    for i in range(0,len(list_one)):
        if list_one[i] == list_two[i]:
            continue
        else:
            result = "They are not the same"
    print result
else:
    print "The lists are not the same."
