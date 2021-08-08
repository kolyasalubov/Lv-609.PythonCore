
import HW711
print ('The area of which figure do you want to calculate?')
figure = int ( input ( 'If the answer is rectangle press 1, triangle - press 2, circle - press 3:\n  ' ))
if figure == 1:
    a = int (input ('Enter a (width):  '))
    b = int(input('b (length):    '))
    print (HW711.sq_rectangle (a,b))
elif figure == 2:
    h = int (input ('Enter h (height):  '))
    a = int(input('a (length):    '))
    print ( HW711.sq_triangle (h,a))
else:
    r = int (input ('Enter r (radius):  '))
    print (round( HW711.sq_circle (r),2))
