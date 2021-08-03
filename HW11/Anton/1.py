class AgeError(Exception):
    def __init__(self, *args):
        if args:    
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return self.message
        else:
            return 'AgeError has been raised'

def even_or_odd(age = 0):
    if age < 0 :
        raise AgeError('age must be positive')
    if age%2 == 0:
        return 'even'
    else:
        return 'odd'
