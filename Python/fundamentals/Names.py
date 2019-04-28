students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

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

def find_names(list):
    for student in list:
        print student['first_name'], student['last_name']

find_names(students)



def find_names_2(dict):
     for keys in dict:
        counter = 0
        print keys
        for each in dict[keys]:
            counter+=1
            f_name = each['first_name'].upper()
            l_name = each['last_name'].upper()
            length = len(f_name) + len(l_name)
            print ('{} - {} {} - {}').format(counter, f_name, l_name, length)

find_names_2(users)