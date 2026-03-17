from models import Animal, Dog, Cat


dog = Dog("Buddy", 3, "Brown", "Labrador")
cat = Cat("Misty", 2, "White", 9)
animal = Animal("Generic", 5, "Gray")


animals = [dog, cat, animal]


for a in animals:
    print(a)
    print(a.speak())
    print(a.info())
    print()
