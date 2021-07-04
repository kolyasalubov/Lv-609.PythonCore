#a=int(input("enter \"a\"-"))
#if a%2==0: print("even number") 
#else:  print("odd number") 


n=2
while n!=102:
    print(n)
    n=n+2

for j in range(101):
   if j % 2==0:
    print(j)

for val in range(101):
       if val % 2==1:
           print(val)

for val in range(101):
       if val % 2==0:
           continue
           print(val)
           