from automobile import Automobile
from factory import Factory

a1 = Automobile("Honda", 10000, True)
a2 = Automobile("Peugeot", 15000, False)
a3 = Automobile("Audi", 20000, False)
a4 = Automobile("BMW", 25000, True)

factory1 = Factory()

factory1.automobile_add(a1)
factory1.automobile_add(a2)
factory1.automobile_add(a4)

factory1.show_factory_info()

factory1.show_all_info()

factory1.automobile_remove(a4)
factory1.show_all_info()
factory1.show_factory_info()
