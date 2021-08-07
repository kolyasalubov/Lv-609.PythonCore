import calculator_def as c

choice=input('   Select the desired action: \n'
             '1-sum \n'
             '2-difference\n'
             '3-product\n'
             '4-division\n'
             '  Your choice - ')

print('Enter numbers:')
x=float(input('x='))
y=float(input('y='))

if choice == '1': c.calculating_sum(x,y)
elif choice == '2': c.calculating_difference(x,y)
elif choice =='3': c.calculating_product(x,y)
elif choice == '4': c.calculating_division(x,y)
else: 
    print('Please enter a valid value: 1, 2, 3, 4')

