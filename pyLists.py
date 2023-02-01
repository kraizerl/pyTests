#Lists / Arrays 
import random

sets = ["R","E","Q","A","P","C"]

sets.sort() #alphabetical sort
#.clear() removes elements from list
#.pop() remove last element
#.append() adds new element

for i in sets:
    print(i, end=" ")
print()
#2d lists/ multidimensional arrays

lunch = ["bread","corn"]
drinks = ["water","soda"]
dessert = ["cake","cok"]

menu = [lunch,drinks,dessert]

print

for i in menu:
    print(i)

nums = []

for i in range(10):
    nums.insert(i,random.randrange(1,200))

print(nums)
print(max(nums))