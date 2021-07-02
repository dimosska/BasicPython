class Person:
    role = 'Person'

    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    def full_name(self):
        return(f'{self.first_name} {self.second_name}')

    def description(self):
        print(f'{self.role} - {self.full_name()}')

class Manager(Person):
    role = 'Manager'


class Administrator(Person):
    role = 'Administrator'


class Developer(Person):
    role = 'Developer'


Person('John', 'Doe').description()
Manager('James', 'Smith').description()
Administrator('Test', 'Admin').description()
Developer('Python', '3').description()
