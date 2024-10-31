class Animal:
    all_animals = []  #! class attr

    def __init__(self, nickname, species, weight, zoo):
        self.nickname = nickname  #! instance attr
        self.species = species  #! instance attr
        self.weight = weight  #! instance attr
        self.zoo = zoo  #! instance attr
        type(self).all_animals.append(self)

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, nickname_str):
        if not isinstance(nickname_str, str):
            raise TypeError("Nickname must be a string")
        self._nickname = nickname_str

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, species_str):
        if not isinstance(species_str, str):
            raise TypeError("Species must be a string")
        elif species_str not in ( "Cat", "Dog", "Rat"):
            raise ValueError("Species must be one of  Cat, Dog, Rat")
        self._species = species_str

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight_str):
        if not isinstance(weight_str, float):
            raise TypeError("Weight must be a string")
        self._weight = weight_str

    @property
    def zoo(self):
        return self._zoo

    @zoo.setter
    def zoo(self, zoo_instance):
        from zoo import Zoo
        if not isinstance(zoo_instance, Zoo):
            raise TypeError("Zoo must be of type Zoo")
        self._zoo = zoo_instance

import ipdb; ipdb.set_trace()