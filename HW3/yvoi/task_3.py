a = "apple"
b = "banana"
print(a, b)
a, b = b, a
print(a, b)

# --- also with numbers we can do this:

a = 20
b = 30
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)