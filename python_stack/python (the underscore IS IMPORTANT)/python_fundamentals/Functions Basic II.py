def countDown(a):
    newlist = []
    for i in range(a, 0, -1):

        newlist.append(i)
    return newlist


print(countDown(9))


def Print_and_Return(list1):
    print(list1[0])
    return list1[1]


print(Print_and_Return([1, 2, 3]))


def First_Plus_Length(list1):
    sum = len(list1)+list1[0]
    return sum

print(First_Plus_Length([1,2,3,4,5]))

def Values_Greater_than_Second(list1):
    max=list1[1]
    newlist=[]
    count=0
    for i in range(0,len(list1),1):
        if list1[i]>max:
            newlist.append(list1[i])
            count+=1
    print(count)
    return newlist
print(Values_Greater_than_Second([1,2,3,4,56,6,2]))


def This_Length_That_Value (size,value):
    newlist=[]
    for i in range(0,size,1):
        newlist.append(value)
    return newlist
print(This_Length_That_Value(5,7))






