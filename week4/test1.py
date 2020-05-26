class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __getitem__(self, item):
        return self.name


user1 = User('don', 'gogi.@asj.com')
print(user1[1])
