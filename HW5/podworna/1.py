print(f'Even numbers that are divisible by 2={[i for i in range(1,11) if i%2==0]}')
print(f'Odd numbers, which are divisible by 3={[i for i in range(1,11) if (i%3!=0) and (i%2!=0)]}')
print(f"Numbers that are not divisible by 2 and 3={[i for i in range(1,11) if (i%3!=0) and (i%2!=0)]}")