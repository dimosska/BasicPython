class Person:
    is_manager = False

    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    def full_name(self):
        print(f'{self.first_name} {self.second_name}')


class Manager(Person):
    is_manager = True
    role = 'Manager'


p1 = Person('John', 'Doe')
p1.full_name()
print(p1.is_manager)


p2 = Manager('Jack', 'Smith')
p2.full_name()
print(p2.is_manager)
