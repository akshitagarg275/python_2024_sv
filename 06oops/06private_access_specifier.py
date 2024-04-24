# __ double underscore is used for private access specifier

class Base:
    def __init__(self):
        self.m = "We are learning python"
        self.__c = "Private variable "


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        # print(self.__c)
        print(self.m)
        

obj = Derived()

