class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return '{} {}'.format(self.__class__, self.name)

if __name__ == "__main__":
    p = Person('Ali')
    print(p)
    print(p.name)
    p.name = 'javad'
    print(p.name)
    p.age = 19
    print(p.age)
    Person.job = 'student'
    print(p.job)
    print(p)