import random 

class Ghost(object):
    palette = ["white", "yellow", "purple", "red"]
    def __init__(self):
        self.color = random.choice(Ghost.palette)
