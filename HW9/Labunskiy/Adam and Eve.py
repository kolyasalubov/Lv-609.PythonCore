class Human(object):
    def __init__(self):
        pass


class Man(Human):
    def __init__(self, name):
        self.name = name


class Woman(Human):
    def __init__(self, name):
        self.name = name


def God():
    adam = Man('Adam')
    eva = Woman('Eva')
    return [adam, eva]


print(God())