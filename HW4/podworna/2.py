list_integer_type=list(input("Enter the list that contains elements of integer type-"))
print(list_integer_type)
j=0
while j!=len(list_integer_type):
  list_integer_type[j]=float(list_integer_type[j])
  print(list_integer_type[j])
  j+=1
