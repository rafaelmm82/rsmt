import numpy as np


class Reservoir:

    def __init__(self, dimension=None, name=None, permeability_i=None,
                 permeability_j=None, permeability_k=None, porosity=None):

        self.dimension = None  # size of x, y, z
        self.name = None  # str with name
        self.permeability_i = None  # 3D array for x, y, z
        self.permeability_j = None  # 3D array for x, y, z
        self.permeability_k = None  # 3D array for x, y, z
        self.porosity = None  # 3D array for x, y, z

    def set_dimension(self, dimension=None):
        pass

    def set_name(self, name=None):
        pass

    def set_permeability(self, direction=None, values=None):
        pass

    def set_porosity(self, values=None):
        pass





