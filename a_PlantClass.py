
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color


class Flower(Plant):                    # Subclass of Plant (it is in parenthesis becasue it is inheriting the attributes)
    def __init__(self,color, petals):
        Plant.__init__(self,color)      # Cannot create a subclass without first creating the superclass
        # __init__ method always has to call superclass before calling subclass
        self.__petals = petals

    def get_petals(self):
        return self.__petals
