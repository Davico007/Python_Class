name = input('What is your name? ')
age =  int(input("What is your age? "))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"{person.name} is {person.age} years old.")


person = Person(name,age)
# print(f"{person.name} is {person.age} years old.")
person.talk()
