import numpy as np


class Reservoir:

    def __init__(self, name=None):
        self.name = name  # str with name


class ReservoirCartesian(Reservoir):

    def __init__(self, name=None, dimension=None, file_header=None):

        super().__init__(name)
        self.dimension = dimension  # size of i, j, k
        self.name = name  # str with name
        self.header = None

        self.initialize(file_header)

        # properties
        # properties are instantiated in 3d numpy array in this sequence
        # z, y, x (k, j, i)
        # the first index is the layer z (k)
        # the second is the row index y (j)
        # the third is the column index x (i)
        # it was defined like that to make easy to retrieve layers content

        # static properties
        self.permeability_i = None  # 3D array z layers
        self.permeability_j = None  # 3D array for x, y, z
        self.permeability_k = None  # 3D array for x, y, z
        self.porosity = None  # 3D array for x, y, z

    def initialize(self, file_header):

        with open(file_header, mode='r') as file_dat_header:
            self.header = file_dat_header.read()


class Well:

    def __init__(self, name=None, x=None, y=None, z=None):
        # initially only one perforation per well
        self.name = name
        self.x = x
        self.y = y
        self.z = z

