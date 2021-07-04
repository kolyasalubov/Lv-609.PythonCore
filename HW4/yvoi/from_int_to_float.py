start = int(input("Enter start value of list: "))
end = int(input("Enter last value of list: "))

my_list = list(range(start, end + 1))
print(f"""This is your list:
{my_list}""")

print("")

i = 0
while i < len(my_list):
    my_list[i] = float(my_list[i])
    i += 1
print(f"""This is changed list (from \"int\" to \"float\"):
{my_list}""")


"""-----RESULT-----
Enter start value of list: 1
Enter last value of list: 10
This is your list:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

This is changed list (from "int" to "float"):
[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
"""