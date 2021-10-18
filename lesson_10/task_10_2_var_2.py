from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, v, h):
        self.material_coat_usage = []
        self.material_costume_usage = []
        self.size = v
        self.height = h

    @abstractmethod
    def material_usage(self):
        pass

    def add_coat_matusage(self, v, h):
        self.material_coat_usage.append(Coat(v, h).material_usage)

    def add_costume_matusage(self,v, h):
        self.material_costume_usage.append(Costume(v, h).material_usage)

    def material_usage(self):
        return sum(self.material_coat_usage)+sum(self.material_costume_usage)

class Coat(Clothes):

    @property
    def material_usage(self):
        return round((self.size/6.5 + 0.5), 2)

class Costume(Clothes):

    @property
    def material_usage(self):
        return round((2*self.height + 0.3), 2)

coat_1 = Coat(5, 6)
print(coat_1.material_usage)
costume_1 = Costume(5, 6)
print(costume_1.material_usage)
print(f'общий расход ткани: {coat_1.material_usage+costume_1.material_usage}')
clothes_1 = Clothes(5,6)
clothes_1.add_coat_matusage(5,6)
clothes_1.add_costume_matusage(5,6)
print(clothes_1.material_usage())



