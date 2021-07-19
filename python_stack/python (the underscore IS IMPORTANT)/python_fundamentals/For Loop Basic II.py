#1 Biggie Size
def Biggie_Size(list1):
    for i in range (0,len(list1),1):
        if list1[i]>0:
            list1[i]="big"
    return list1
print(Biggie_Size([-1,-2,3,4,5,-4]))


#2 Count Positives
def Count_Positives(list1):
    count=0
    for i in range(0,len(list1),1):
        if list1[i]>0:
            count+=1
    list1[len(list1)-1]=count
    return list1
print(Count_Positives([-1,-2,3,4,5,-4]))

#3 Sum Total
def Sum_Total(list1):
    sum=0
    for i in range(0,len(list1),1):
         sum+=list1[i]
    return sum
print(Sum_Total([3,4,5]))
    
#4 Average 
def Average (list1):
   return Sum_Total(list1)/len(list1)


print(Average([3,4,5]))


#5 Length
def Length (list1):
    return len(list1)
print(Length([3,4,5]))



#6 Minimum
def Minimum(list1):
    min=list1[0]
    if len(list1)==0:
        return False
    elif len(list1)==1:
        return list1
    else:
        for i in range (0,len(list1),1):
            if list1[i]<min:
                min=list1[i]
        return min
print(Minimum([3,4,5]))

#7 Maximum 
def Maximum (list1):
    max=list1[0]
    if len(list1)==0:
        return False
    elif len(list1)==1:
        return list1
    else:
        for i in range (0,len(list1),1):
            if list1[i]>max:
                max=list1[i]
        return max
print(Maximum([3,4,5]))

#8 Ultimate Analysis  
def Ultimate_Analysis(list1): 
    myDictonary = {'sumTotal': Sum_Total(list1), 'average': Average(list1), 'minimum': Minimum(list1), 'maximun': Maximum(list1), 'length': len(list1)}
    return myDictonary
print(Ultimate_Analysis([3,4,5]))


#9 Reverse List 
def Reverse_List(list1):
    for i in range(0,(len(list1)-1)//2):
            temp = list1[i]
            list1[i] = list1[len(list1)-1-i]
            list1[len(list1)-1-i] = temp
    return list1
print(Reverse_List([3,4,5,7,8,9]))


