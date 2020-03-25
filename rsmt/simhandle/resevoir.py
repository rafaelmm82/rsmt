from .templates.imex_data import imex_spe9_header


class Reservoir:

    def __init__(self, name=None):
        self.name = name  # str with name


class ReservoirCartesian(Reservoir):

    def __init__(self, name=None, dimension=None, template=None):

        super().__init__(name)
        self.dimension = dimension  # size of i, j, k

        if template == 'spe9':
            self.header = imex_spe9_header
        else:
            self.header = None

