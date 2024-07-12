
#given list
list1 = [2, 51, 11, 13, 51, 100]





# 1. output every item from list with positive indexing
for i in range(len(list1)):
    print(list1[i],end=' ')
print()

     







# 2  output every item from list with negative indexing
for i in range(-1, -len(list1)-1, -1):
    print(list[i], end=' ')
    print()




    
#3 replace the last element of a list with a new value
list1[-1]=999
print("list after replacing last elment:",list1)





#4 replace the fifth element  of a list with a new value 
if len(list1) >=5:
    list1[4] = 777
    print("list after replacing fifth element.")
else:
    print("list doesn't have a fifth element.")







    
# 5 extract the last three elements of a list.
last_three = list1[-3:]
print("last three elements:",last_three)









# 6 extract the first three elements of a list. 
first_three = list1[-3:]
print("first three elements:",first_three)









# 7 extract the middle two elements of a list.<[11, 13]>
if len(list1) >= 4:
    middle_two = list1[2:4]
    print("middle two elements:", middle_two)
else:
    print("list doesn't have enough elements for middle extraction.")







    
#8 extract random elements of list with negative indexes.
random_elements = list1[-3:-1] # extract elements from the third last to second last
print("random elements with negative indexes:", random_elements)
