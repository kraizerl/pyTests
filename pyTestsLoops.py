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