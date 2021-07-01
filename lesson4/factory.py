class Factory:
    def __init__(self):
        self.automobile_count = 0
        self.automobile_assembled_count = 0
        self.automobile_info = []

    def automobile_add(self, automobile):
        self.automobile_count += 1
        if automobile.is_assembled:
            self.automobile_assembled_count += 1
        self.automobile_list = (
            automobile.name, automobile.price, automobile.is_assembled)
        self.automobile_info.append(self.automobile_list)

    def automobile_remove(self, automobile):
        self.automobile_count -= 1
        if automobile.is_assembled:
            self.automobile_assembled_count -= 1
        self.automobile_list = (
            automobile.name, automobile.price, automobile.is_assembled)
        self.automobile_info.remove(self.automobile_list)

    def show_factory_info(self):
        print(
            f'There are {self.automobile_count} cars in factory\nThere are {self.automobile_assembled_count} assembled cars in factory')
    

    def show_all_info(self):
        print('Automobiles in factory now:')
        for element in self.automobile_info:
            print(element)
