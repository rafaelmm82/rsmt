import numpy as np


class Reservoir:

    def __init__(self, dimension=None, name=None):

        self.dimension = dimension  # size of x, y, z
        self.name = name  # str with name
        self.permeability_i = None  # 3D array for x, y, z
        self.permeability_j = None  # 3D array for x, y, z
        self.permeability_k = None  # 3D array for x, y, z
        self.porosity = None  # 3D array for x, y, z

    def set_dimension(self, dimension=None):

        if len(dimension) == 3:
            if dimension == self.dimension:
                print('Reservoir not changed: same dimension was given')
            else:
                self.dimension = dimension
                print('Reservoir dimension changed, properties must be redefined')
                print('Reservoir new dimensions: i={}, j={}, k={}'
                      .format(self.dimension[0],
                              self.dimension[1],
                              self.dimension[2]))
        else:
            print('Reservoir dimension not defined: wrong dimension parameter')

    def set_name(self, name=None):

        if type(name) == str:
            self.name = name
        else:
            print('Reservoir name not changed: invalid value')

    def set_permeability(self, direction=None, values=None):

        # check the direction of permeability and dimension compatibility
        if direction in ['i', 'j', 'k'] and values.shape == self.dimension:
            pass
        else:
            pass

    def set_porosity(self, values=None):

        # check dimensional compatibility
        if values.shape == self.dimension:
            pass
        else:
            pass





