def check(x):
    try:
        if type(x)!=int:
            raise TypeError
        elif x < 0:
            raise ValueError
        return "Your age is odd" if x%2!=0 else "Your age is even"
    except TypeError:
        return "Your age must be an integer!"
    except ValueError:
        return "Your age can't be less than 0!"

print(check(-12))
