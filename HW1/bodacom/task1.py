# HW1\bodacom\task1.py 
# Done

# Output questions
# “What is your name?“, 
# “How old are you?“, 
# “Where do you live?“. 
# Read the answer of user and output next information: 
# “Hello, (answer(name))“, 
# “Your age is  (answer(age))“, 
# “You live in  (answer(city))“.  

# Questionaire
name = input('What is your name?: ')
age = input('How old are you?: ')
city = input('Where do you live?: ')

# Print info
print("\nHello, %s" % name)
print("Your age is %s" % age)
print("You live in %s" % city)
print()