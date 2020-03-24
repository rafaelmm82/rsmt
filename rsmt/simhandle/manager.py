import os


class Manager:

    def __init__(self, work_dir=None):

        self.work_dir = work_dir

        self.reservoir = None
        self.project = None
        self.wells = None

    def setup(self, reservoir, project, wells):
        self.reservoir = reservoir
        self.project = project
        self.project.work_dir = self.work_dir
        self.wells = wells

    def generate_files(self):
        # create directory with instances names (wells for now)
        os.chdir(self.work_dir)

        file_well_head = self.project.generate_well_header()
        file_well_time_steps = self.project.generate_time_steps()

        for e, i in enumerate(self.project.instances):
            # create sim input files
            os.mkdir(i.name)
            os.chdir(self.work_dir + "/" + i.name)
            file_name = self.reservoir.name + '_' + self.project.name \
                        + '_' + i.name + '.dat'
            with open(file_name, mode='w') as file_sim:
                file_sim.write(self.reservoir.header)
                file_sim.write(file_well_head)
                file_sim.write(self.project.generate_well_entry(e))
                file_sim.write(file_well_time_steps)

            os.chdir(self.work_dir)

            # create sim output extract file

    def execute_project(self, run=None):
        pass

    def retrieve_data(self, run=None):
        pass

