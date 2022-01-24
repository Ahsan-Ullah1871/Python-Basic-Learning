class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi {self.name} ! How are you")

person1 = Person("Ahsan")
person1.talk()
