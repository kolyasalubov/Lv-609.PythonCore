number = int(input('enter the number'))
f= 1
while number>1:
    f = f * number
    number= number - 1
print ('factorial',f)