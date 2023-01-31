#useful py syntax
import math
import time


#name = "1"
#name = int(name) Cast in py


#Slicing creates substrings [start=index:stop:step=order]

#name = "Otravigus"
#reversedName = name[::-1] 
#print(reversedName)

#   slice
#website = "http://google.com"
#slice = slice(7,-4)
#print(website[slice])

# if statments in py , indentation important
#age = int(input("How old are you:"))

#if age >=21:
#    print("Access Granted")
#else:
#    print("Error: Invalid age")

# logic in py (and, or , not)
#if age >21 and age <30 or age == 20:
 #   print("Young")
#elif not(age < 60):
 #   print("old")

# while loop in py, executes as long as true
#name = None
#while not name:
 #   name = input("Enter name:")

# for loops in py
#for i in range(10):  # JAva == for(int i = 0;i>=10;i++)
 #   print(i)

#for i in range(10,0,-1): #// starts at 10, stops at 0, increases by -1
 #   print(i)

#for i in "Coke":
 #   print(i)

#for secs in range(10,0,-1):
#    print(secs)
#    time.sleep(1)
#print("POGGERS")

#NESTED LOOPs just like jAva
rows = int(input("Input Rows:"))
columns = int(input("Input Columns:"))
symbol = input("Input Symbol:")

for i in range(rows): #outer loop i
    for j in range(columns): #inner loop j
        print(symbol, end="")
    print()