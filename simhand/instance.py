

class Well:

    def __init__(self, reservoir=None, pos=None, perforations=None):

        self.reservoir = reservoir
        self.pos = pos
        self.perforations = perforations

    def define_position(self, pos=None):
        pass

    def define_perforations(self, perforations=None):
        pass


class Instance:

    def __init__(self, reservoir=None):
        pass

