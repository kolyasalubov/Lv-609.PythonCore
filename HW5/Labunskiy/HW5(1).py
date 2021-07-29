def count_int_fetch(numbr):
    counter_even = sum(1 for digit in range(1, numbr+1) if digit % 2 == 0)
    counter_not_even = sum(1 for digit in range(1, numbr+1) if digit % 3 == 0)
    counter_other = sum(1 for digit in range(1, numbr+1)
                              if digit % 3 != 0 and digit % 2 != 0)
    return f"Count event digits is {counter_even},"\
           f" count not event digits is {counter_not_even},"\
           f" count other digits is {counter_other}."


print(count_int_fetch(int(input("Enter the number : "))))
