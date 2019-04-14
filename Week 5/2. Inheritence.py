class Employee:
    def __init__(self, fullname, job, salary):
        self.fullname = fullname
        self.job = job
        self.salary = salary
    def __str__(self):
        return '{} {}-{}'.format(self.__class__, self.fullname, self.job)
    def getLastName(self):
        return self.fullname.split()[-1]
    def giveRaise(self, percentage):
        self.setSalery(self.salary + percentage * self.salary)
    def setSalery(self, salary):
        self.salary=salary
    def getSalery(self):
        return self.salary

class Manager(Employee):
    def __init__(self, fullname, job, salary, rank):
        Employee.__init__(self, fullname, job, salary)
        self.rank = rank

    def giveRaise(self, percentage):
        Employee.giveRaise(self, percentage + .05)

if __name__ == "__main__":
    e = Employee('Alex Morgan', 'Dev', 250000)
    print(e)
    print(e.getLastName())
    e.giveRaise(.1)
    print(e.salary)
    e.setSalery(250000)
    print(e.getSalery())

    m = Manager('Kambiz Dirbaz', 'Manager', 300000, 3)
    print(m)
    print(m.rank)
    print(m.getSalery())
    m.giveRaise(.1)
    print(m.getSalery())