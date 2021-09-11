#HW4 task 2
# Done

#Task2. Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type. 
#(Hint: use the built-in float () function). 

list_integer = list(int(i) for i in range(0,257,3))

i = 0
for l in list_integer:
    list_integer[i] = float(l)
    i+=1
print(list_integer)
