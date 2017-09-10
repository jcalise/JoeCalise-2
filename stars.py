def stars(list):
    for item in list:
        val = ""
        for i in range(0,item):
            val += "*"
        print val

x = [4, 6, 1, 3, 5, 7, 25]
# stars(x)


def modifiedStars(list):
    for item in list:
        if isinstance(item,int):
            val = ""
            for i in range(0,item):
                val += "*"
            print val
        else:
            val = ""
            char = item[0].lower()
            length = len(item)
            for i in range(0,length):
                val += char
            print val

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
modifiedStars(x)
