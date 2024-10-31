from animal import Animal

# Zoo() -> __create__ -> __init__
class Zoo:
    all_zoos = [] #! class attr

    def __init__(self, name, location):
        self.name = name #! instance attr
        self.location = location  #! instance attr
        type(self).all_zoos.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_str):
        if not isinstance(name_str, str):
            raise TypeError("Name must be a string")
        self._name = name_str

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location_str):
        if not isinstance(location_str, str):
            raise TypeError("Location must be a string")
        self._location = location_str

    def animals(self):
        return [animal for animal in Animal.all_animals if animal.zoo is self]

import ipdb; ipdb.set_trace()
