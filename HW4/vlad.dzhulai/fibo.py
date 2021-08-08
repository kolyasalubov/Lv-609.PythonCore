#Logic when we are entering a quantity of numbers fibo to be shown
# def fibo_print_numbers:
#     fibo_number = int(input("Enter a fibo number: "))
#     fibo_list = []
#     for i in range(fibo_number+1):
#         if i == 0:
#             fibo_list.append(0)
#         elif i == 1:
#             fibo_list.append(1)
#         else:
#             fibo_list.append(fibo_list[-1]+fibo_list[-2])
#     print(fibo_list)

#The right logic for a program:
fibo_number = int(input("Enter a fibo number: "))
fibo_list = [0, 1]
if fibo_number == 0:
    print([0])
elif fibo_number == 1:
    print([0, 1])
else:
    while fibo_list[-1] < fibo_number:
        fibo_list.append(fibo_list[-1]+fibo_list[-2])
    if fibo_list[-1] >= fibo_number:
        fibo_list.pop()
    print(fibo_list)