def factorial(number: int):
    temp_num = 1
    for i in range(1, number + 1):
        temp_num *= i
    return temp_num
    
    

if __name__ == "__main__":
    print(factorial(5))