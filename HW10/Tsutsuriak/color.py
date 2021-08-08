import random
list1 = ['white', 'yellow', 'purple', 'red']

class Ghost(object):
    
    def __init__(self):
        self.color = random.choice(list1)
 