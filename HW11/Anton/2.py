
nums = ['1', '2', '3', '4', '5', '6', '7']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
num_day = dict(zip(nums, days))

class NumberError(Exception):
    def __init__(self, mes = None):
        self.message = mes
    def __str__(self):
        print('NumberError has been raised')
        return self.message

def day_by_number(num):
    if num <= 0 or num >= 8:
        raise NumberError('only [1-7] are valid')
    else: 
        return num_day[str(num)]
