for i in range (151): #Basic - Print all integers from 0 to 150.
    print(i)

for a in range(5,1001,5):#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
    print(a)

for b in range(1,101,1):#Counting, the Dojo Way
    if b % 5 == 0:
        print("Coding")

    else:
         print("Coding Dojo")
sum = 0
for s in range(0,500000,1):#Whoa. That Sucker's Huge
    if s % 2 != 0:
        sum=sum+s
print(sum)

for f in range(2018,0,-4):#Countdown by Fours 
    print(f)

lowNUM=2
HighNum=9
Mult=3
for g in range(lowNUM,HighNum+1,1):#Flexible Counter
    if g % Mult == 0:
      print(g)

