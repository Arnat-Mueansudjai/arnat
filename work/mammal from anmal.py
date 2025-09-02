from Zoo.animal import Animal


class Mammal(Animal):

    def __init__(self, name):
        super().__init__(name)
        #Super= Animal 
        #__init__ = method of Animal

class Bear(Mammal):

    def __init__(self, name):
        super().__init__(name)

class Gorilla(Mammal):

    def __init__(self, name):
        super().__init__(name)