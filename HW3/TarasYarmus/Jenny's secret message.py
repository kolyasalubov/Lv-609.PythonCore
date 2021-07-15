def greet(name):
    if name == "Johnny":
        return print ("Hello, my love!")
    else:
        return print (f"Hello, {name}!")

name = input('Enter your name:')
greet(name)