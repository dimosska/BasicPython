from .person import Person
from .company import Company

p1 = Person('John', 'Doe')
p2 = Person('James', 'Smith')
p3 = Person('James2', 'Smith2')
p4 = Person('James3', 'Smith3')
p5 = Person('James4', 'Smith4')

company=Company()

company.add_person(p1)
company.add_person(p3)
company.add_person(p4)

company.show_people()

