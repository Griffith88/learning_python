class Pet:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Cat(Pet):
    def __init__(self,name,weight,shmups=True):
        super().__init__(name, weight)
        self.shmups = shmups or []

    def say(self):
        return '{} say mrmmrmrmrm with weight {}, is he SHMUPSIK PUPSIK??? Answer = {} '.format(self.name,self.weight,self.shmups)

cat = Cat('Zhihar', '4kg')
print(cat.say())
