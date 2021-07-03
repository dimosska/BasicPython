class Car:
    name = None
    carlist = []

    def __init__(self, price, is_assembled):
        self.price = price
        self.is_assembled = is_assembled
        Car.carlist.append(self)

    @property
    def car_info(self):
        return f'{self.name} {self.price}\t{self.is_assembled}'

    @staticmethod
    def show_all_info():
        for cars in Car.carlist:
            print(f'{cars.name}\t{cars.price}\t{cars.is_assembled}')


class Mercedes(Car):
    name = 'Mercedes'


class Audi(Car):
    name = 'Audi'


class Peugeot(Car):
    name = 'Peugeot'


class BMW(Car):
    name = 'BMW'


class Factory:
    counter = 0
    assembled_counter = 0

    def __init__(self):
        self.cars = []

    def add_car(self, car):
        if self.counter < 3:
            self.cars.append(car)
            self.counter += 1
            if car.is_assembled:
                self.assembled_counter += 1
        else:
            print('There are no more place in factory')

    def remove_car(self, car):
        self.counter -= 1
        self.cars.remove(car)
        if car.is_assembled:
            self.assembled_counter -= 1

    def assemble(self, car):
        if car.is_assembled == False:
            car.is_assembled = True
            self.assembled_counter += 1

    def show_info(self):
        return f'{self.counter} cars onboard. {self.assembled_counter} cars are assembled'


c1 = Mercedes(10000, True)
c2 = Audi(12000, False)
c3 = Peugeot(10400, True)
c4 = BMW(15000, False)

f1 = Factory()

f1.add_car(c1)
f1.add_car(c2)
f1.add_car(c3)
f1.add_car(c4)
print(f1.show_info())
f1.remove_car(c1)
print(f1.show_info())
