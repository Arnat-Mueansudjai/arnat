class Animal:
    #Constructor
    def __init__(self, name):
        self.name = name

class Reptile(Animal):

    def __init__(self, name):
        super().__init__(name)   

class Mammal(Animal):

    def __init__(self, name):
        super().__init__(name)

class Bear(Mammal):

    def __init__(self, name):
        super().__init__(name)

class Gorilla(Mammal):

    def __init__(self, name):
        super().__init__(name)