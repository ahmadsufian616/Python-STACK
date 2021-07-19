#1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0]=15 # list inside list  list=[list,list]
print(x) #Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
students[0]['last_name']='Bryant' # dictionaries  inside list  list=[dictionaries ,dictionaries ]
print(students[0]['last_name'])#Change the last_name of the first student from 'Jordan' to 'Bryant'
sports_directory['soccer'][0]='Andres' # is like  dictionaries and list [key][list]
print(sports_directory['soccer'][0])#In the sports_directory, change 'Messi' to  'Andres'
z[0]['y']=30
print(z)#Change the value 20 in z to 30 list[dictionaries]
###################################################################################################################################

#2


def iterateDictionary(list1):
    for i in range(0,len(list1),1):
        for key in list1[i]:
            print(key," - ",list1[i][key],"  ",end = " ")
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
###################################################################################################################################
#3
def iterateDictionary2(key_name,list1):
    for i in range(0,len(list1),1):
       print(list1[i][key_name])
iterateDictionary2("first_name",students)
iterateDictionary2("last_name",students)
###################################################################################################################################

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# #printInfo(dojo)
# # output:
# #7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

def printInfo (dic1):
    for k in dic1:
       print(len(dic1[k]),k)
       for val in dic1[k]:
            print(val)
printInfo(dojo)