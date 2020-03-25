
class Well:

    def __init__(self, name=None, x=None, y=None, z=None):
        # initially only one perforation per well
        self.name = name


class VerticalWell(Well):

    def __init__(self, name=None, x=None, y=None, z=None):
        # initially only one perforation per well
        super().__init__(name)
        self.x = x
        self.y = y
        self.z = z
