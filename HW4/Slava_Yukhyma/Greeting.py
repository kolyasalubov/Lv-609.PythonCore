

stop_num = 24
list_fib = [0, 1]
i = 0
where_to_stop = 1
while where_to_stop != stop_num:
    fib_num = list_fib[i] = list_fib[i+1]
    list_fib.append(fib_num)
    i += 1
    where_to_stop += 1
print(list_fib)
