def dictToTuple(dict):
    tupList = []
    for key,item in dict.iteritems():
        tuple = (key,item)
        tupList.append(tuple)
    return tupList


my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

print dictToTuple(my_dict)
