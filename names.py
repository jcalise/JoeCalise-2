students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def printStudents(dict):
    for d in dict:
        print d['first_name'] + " " + d['last_name']

# printStudents(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printUsers(dict):
    for k,v in dict.iteritems():
        print k
        num = 1
        for d in v:
            total = len(d['first_name']) + len(d['last_name'])
            print  str(num) + " " + d['first_name'] + " " + d['last_name'] + " - " + str(total)
            num += 1

printUsers(users)
