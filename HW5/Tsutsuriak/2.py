login = str(input("Enter your login: "))
code_word = "First"
if code_word == login:
    print("Hello, First!")
while code_word != login:
    login = str(input("Wrong. Enter your login: "))
print("Hello, First!")
