def check_num(num):
    "returns the day of the week"
    list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    try:
        if type(num)!=int:
            raise TypeError
        elif num not in range(1,8):
            raise ValueError
        return list[num-1]
    except ValueError:
        return "Value should be between 1 and 7"
    except TypeError:
        return "You should input an integer"

print(check_num(5))