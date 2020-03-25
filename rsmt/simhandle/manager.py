import os
from .project import Project
from .templates.imex_data import imex_well_header, imex_well_each, imex_time_step

report_exe = "C:\\Program Files (x86)\\CMG\\BR\\2015.10\\Win_x64\\EXE\\report.exe"
simulator_exe = "C:\\Program Files (x86)\\CMG\\IMEX\\2015.10\\Win_x64\\EXE\\mx201510.exe"


class Manager:

    def __init__(self, work_dir=None, project=None, simulator_bin=simulator_exe, report_bin=report_exe):

        self.work_dir = work_dir
        self.project = project
        self.project_path = None

        self.simulator_bin = simulator_bin
        self.report_bin = report_bin

    def setup_simulation(self):
        # create directory with instances names (wells for now)
        self.project_path = os.path.join(self.work_dir, self.project.name)
        os.mkdir(self.project_path)
        os.chdir(self.project_path)

        file_time_steps = self._dat_file_time_steps()

        # for each simulation generate folder, dat file and rwd file
        for sim in self.project.simulations:

            sim_path = os.path.join(self.project_path, 'sim_' + sim.name)
            os.mkdir(sim_path)
            os.chdir(sim_path)

            # dat file
            filename_dat = '_'.join([self.project.name, sim.name, '.dat'])
            with open(filename_dat, mode='w') as file_dat:
                file_dat.write(self.project.reservoir.header)
                file_dat.write(imex_well_header)
                for w in sim.wells:
                    file_dat.write(self._dat_file_well_entry(w))
                file_dat.write(file_time_steps)

            # rwd file
            filename_rwd = '_'.join([self.project.name, sim.name, '.rwd'])
            with open(filename_rwd, mode='w') as file_rwd:
                file_rwd.write()
                file_rwd.write()
                file_rwd.write()
                file_rwd.write()

            # report folders
            os.mkdir('well_data')
            os.mkdir('static_data')
            os.mkdir('dynamic_data')
            os.chdir(self.project_path)

###

            with open(file_name_extract, mode='w') as file_ext:
                file_ext.write(self.project.generate_sim_output_extract_file(e+1))

            # create extract file directories
            os.mkdir('gas_saturation')
            os.mkdir('oil_saturation')
            os.mkdir('water_saturation')
            os.mkdir('pressure')
            os.mkdir('static')

            os.chdir(self.work_dir)

            # create sim output extract file

    def execute_project(self, run=None):
        # TODO: python exec with partial report
        # report_exe = 'C:\Users\magalraf\Documents\GitHub\rsmt\test_sim\Producer9>"C:\Program Files (x86)\CMG\BR\2015.10\Win_x64\EXE\report.exe"  -f "spe9_onewell_z3_Producer9.rwd"  -o sim_9_permeability_i.rwo'
        # simulator_exe = 'C:\Users\magalraf\Documents\GitHub\rsmt\test_sim\Producer19>"C:\Program Files (x86)\CMG\IMEX\2015.10\Win_x64\EXE\mx201510.exe"  -f "spe9_onewell_z3_Producer19.dat" -wd "C:\Users\magalraf\Documents\GitHub\rsmt\test_sim\Producer19" -wait'

        pass

    def retrieve_data(self, run=None):
        pass

    def _dat_file_time_steps(self):
        t_steps = "\n".join(["*TIME {}\n".format(t)
                             for t in self.project.time_steps])
        return imex_time_step.format(times_list=t_steps)

    @staticmethod
    def _dat_file_well_entry(well=None):
        return imex_well_each.format(well_name=well.name,
                                     x=well.x,
                                     y=well.y,
                                     z=well.z)