factorial_input=int(input("Enter the number=")) 
j=1
factorial_exit=1
while j in range(1,factorial_input):
    j+=1
    factorial_exit=(factorial_exit*j)
print(f"!{factorial_input}={factorial_exit}")