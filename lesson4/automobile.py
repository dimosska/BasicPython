class Automobile:
    auto_list = []

    def __init__(self, name, price, is_assembled):
        self.name = name
        self.price = price
        self.is_assembled = is_assembled
        Automobile.auto_list.append(self)

    def show_info(self):
        print(f'{self.name} {self.price} {self.is_assembled}')

