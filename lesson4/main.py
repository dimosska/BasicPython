from automobile import Automobile
from factory import Factory

a1 = Automobile("Honda", 10000, True)
a2 = Automobile("Peugeot", 15000, False)
a3 = Automobile("Audi", 20000, False)
a4 = Automobile("BMW", 25000, True)

fact = Factory()

fact.automobile_add(a1)
fact.automobile_add(a2)
fact.automobile_add(a4)

fact.show_factory_info()

fact.show_all_info()

fact.automobile_remove(a4)
fact.show_all_info()
fact.show_factory_info()
