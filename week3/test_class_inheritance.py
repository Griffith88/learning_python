class Pet:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Cat(Pet):
    def __init__(self,name,shmups=True):
        self.name = name
        self.shmups = shmups or []

    def say(self):
        return '{} say mrmmrmrmrm'.format(self.name)
