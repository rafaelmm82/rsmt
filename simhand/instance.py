import numpy as np


class Well:

    def __init__(self, reservoir=None, name=None, pos=None, perforations=None):

        self.reservoir = reservoir
        self.pos = pos
        self.name = name
        self.perforations = perforations

    def set_position(self, pos=None):
        pass

    def set_perforations(self, perforations=None):
        pass

    def set_name(self, name=None):
        pass


class Instance:

    def __init__(self, reservoir=None, wells=None, time_steps=None):

        self.wells = wells  # an array of Well objects
        self.time_steps = None  # an array with all time days in the instance
        self.state = dict()  # an dict to store dynamic state properties

    def add_well(self, well=None):
        pass

    def remove_well(self, well_name=None):
        pass

    def set_time_steps(self, time_steps=None):
        pass

    def set_state_property(self, state_prop=None, time_step=None, values=None):
        pass

