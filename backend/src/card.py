class Abstract_card:

    def __init__(self,desc):
        self.desc = desc

    def __str__(self):
        return self.desc

class Abstract_colored_card(Abstract_card):

    def __init__(self,color,value):
        super().__init__(f"{value} de {color}")

class Belote_card(Abstract_colored_card):

    values = ["sept","huit","neuf","dix","valet","dame","roi","as"]
    colors = ["carreau","coeur","pique","trefle"]

    def __init__(self,color,value):
        if value in self.values:
            self.value = self.values.index(value)
        else:
            raise ValueError(f"{value} is not in {self.values}")

        if color in self.colors:
            self.color = self.colors.index(color)
        else:
            raise ValueError(f"{color} is not in {self.colors}")

        super().__init__(color,value)
