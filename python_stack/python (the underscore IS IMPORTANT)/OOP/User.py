#The Minion Game
# def minion_game(string):
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     score_kevin = 0
#     score_stuart = 0
        
#     for ind in range(len(string)):
#         if string[ind] in vowels:
#             score_kevin += len(string) - ind
#         else:
#             score_stuart += len(string) - ind
        
#     if score_kevin > score_stuart:
#         print("Kevin {}".format(score_kevin))
#     elif score_kevin < score_stuart:
#         print("Stuart {}".format(score_stuart))
#     else:
#         print("Draw")
# minion_game("banana")

# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])

# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))



# #initialising an empty list!
# marksheet = [] 

# #iterating through a for loop starting from zero, to some user input(default type string) - that is converted to int
# for i in range(0,int(input())): 
#     #appending user input(some string) and another user input(a float value) as a list to marksheet
#     marksheet.append([raw_input(), float(input())]) 

# #[marks for name, marks in marksheet] - get all marks from list
# #set([marks for name, marks in marksheet]) - getting unique marks
# #list(set([marks for name, marks in marksheet])) - converting it back to list
# #sorting the result in decending order with reverse=True and getting the value as first index which would be the second largest.
# second_highest = sorted(list(set([marks for name, marks in marksheet])),reverse=True)[1] 

# #printing the name and mark of student that has the second largest mark by iterating through the sorted list.
# #If the condition matches, the result list is appended to tuple  -`[a for a,b in sorted(marksheet) if b == second_highest])` 
# #now join the list with \n - newline to print name and mark of student with second largest mark
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))


# cube = lambda x: pow(x,3)
# def fibonacci(n):
#      list1 = [0,1]
#      for i in range(2,n):
#          list1.append(list1[i-2] + list1[i-1])
#      return list1
# print(fibonacci(5))
# print(cube)



# cube = lambda x: pow(x,3) 
# def fibonacci(n):
#     lis = [0,1]
#     for i in range(2,n):
#         lis.append(lis[i-2] + lis[i-1])
#     return(lis[0:n])

#    if __name__ == '__main__':
#     n = int(raw_input())
#     print map(cube, fibonacci(n))




n, m = raw_input().split()