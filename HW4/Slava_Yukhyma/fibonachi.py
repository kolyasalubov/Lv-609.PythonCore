
#######################################################################
user_number = int(input('enter your number: '))
list_fib=[0, 1]
where_to_stop = 1
i = 0
while where_to_stop != user_number:
    fib_num = list_fib[i] + list_fib[i+1]
    list_fib.append(fib_num)
    i+=1
    where_to_stop+=1
print(list_fib)
##############################################################################
number_by_user = int(input('Enter your number: '))
counter = 1
i = 0
list_of_fib = [0,1]
for i in range(number_by_user+1):
    if counter <= number_by_user:
        fib_number = list_of_fib[i] + list_of_fib[i+1]
        list_of_fib.append(fib_number)
        i+=1
        counter += 1
print(list_of_fib)






