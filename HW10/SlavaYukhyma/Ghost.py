from random import choice


class Ghost(object):
    color = ''

    def __init__(self):
        colors = ['white',  'yellow', 'purple', 'red']
        self.color = choice(colors)


a = Ghost()
b = Ghost()
c = Ghost()
print(a.color)
print(b.color)
print(c.color)
