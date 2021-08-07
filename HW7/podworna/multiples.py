def solution(number):
    list_of_number=[x for x in range(1,number) if x%3==0 or x%5==0]
    return sum(list_of_number)
  