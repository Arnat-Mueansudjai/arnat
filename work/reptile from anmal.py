from Zoo.animal import Animal


class Reptile(Animal):

    def __init__(self, name):
        super().__init__(name)


class Snake(Reptile):

    def __init__(self, name):
        super().__init__(name)


class Lizard(Reptile):

    def __init__(self, name):
        super().__init__(name)