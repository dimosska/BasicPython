class Person:
    def __init__(self, first_name, second_name):
        self.first_name=first_name
        self.second_name=second_name

    def full_name(self):
        print(f'{self.first_name} {self.second_name}')