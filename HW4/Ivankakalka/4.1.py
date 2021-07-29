enter_num = int (input ("Enter number: "))
factorial = 1
if enter_num >= 0:
    for fact in range(1,enter_num+1):
        factorial*=fact
    print (factorial)
else:
    print ("Enter number, that is >= 0")