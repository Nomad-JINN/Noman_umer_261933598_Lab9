class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def Display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class House():
    def __init__(self,address,no_of_rooms):
        self.address = address
        self.rooms = no_of_rooms
        self.People_Living_Inside = []

    def Display(self):
        print("Adress:",self.address)
        print("Number of Rooms:",self.rooms)
        print("following are the people living in the house:")
        for x in self.People_Living_Inside:
            x.Display()

    def Add_Person(self,person):
        self.People_Living_Inside.append(person)

    def Remove_Person(self,person):
        self.People_Living_Inside.remove(person)


p1 = Person("Alex",18)
h1 = House("sjhgfiwguofe",7)

h1.Add_Person(p1)
h1.Display()
