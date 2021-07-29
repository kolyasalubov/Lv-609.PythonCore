name = input("What is your name? ")
age = input("How old are you? ")
city = input("Where do you live? ")

print("Hello, %s!" % (name))
print("Your age is % s!" % (age))
print("You live in  %s!" % (city))

print("Hello, {}!".format(name))
print("Your age is {}!".format(age))
print("You live in  {}!".format(city))

print(f"Hello, {name}!")
print(f"Your age is {age}!")
print(f"You live in  {city}!")
