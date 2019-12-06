

class Project:

    def __init__(self, reservoir=None, instances=None, time_steps=None):

        self.work_dir = None  # disk_relative path
        self.reservoir = reservoir  # Reservoir object reference
        self.instances = instances  # array of instances
        self.time_steps = time_steps  # array of ints for each day number

    def set_reservoir(self, reservoir=None):
        pass

    def add_instance(self, instance=None):
        pass

    def set_sim_reference_file(self, file=None):
        pass

    def set_sim_prefix_name(self, name=None):
        pass

    def generate_sim_input_files(self):
        pass

    def generate_sim_output_files(self):
        pass

    def load_sim_results(self):
        pass

    def load_pickle(self, file=None):
        pass

    def dump_pickle(self, file=None):
        pass


