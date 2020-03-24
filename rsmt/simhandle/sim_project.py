

class SimProject:

    def __init__(self, name=None, reservoir=None, instances=None, time_steps=None):

        # initially each run has only one producer well
        self.name = name
        self.work_dir = None
        self.reservoir = reservoir  # Reservoir object reference
        self.instances = instances  # array of wells for each instances
        self.time_steps = time_steps  # array of ints for each day number

    def generate_time_steps(self):
        time_steps = "\n**************\n** TIME STEPS\n**************\n\n"

        for t in self.time_steps:
            time_steps += "*TIME {}\n".format(t)

        time_steps += "\n*STOP\n"

        return time_steps

    @staticmethod
    def generate_well_header():

        well_header =  \
            """
********************************************************************************
** Well and Recurrent Data Section                                            **
********************************************************************************

*RUN

*DATE 1980 01 01
*DTWELL 1.00
*AIMWELL *WELLNN

*GROUP 'ALL-WELLS' *ATTACHTO 'FIELD'

            """
        return well_header

    def generate_well_entry(self, inst):

        well_text = \
            """
*********
** WELLS
*********

** For each well
*WELL '{}' *VERT {} {} *ATTACHTO 'ALL-WELLS'
*PRODUCER '{}'
*OPERATE *MIN *BHP 1000. CONT

**          rad  geofac  wfrac  skin
**             rad  geofac  wfrac   skin
*GEOMETRY  *K  0.5  0.355   1.0     0.0
*PERF      *GEO  '{}'

** UBA            ff   Status  Connection
{} {} {}   1.0  OPEN   FLOW-TO 'SURFACE' REFLAYER

            """.format(self.instances[inst].name,
                       self.instances[inst].x,
                       self.instances[inst].y,
                       self.instances[inst].name,
                       self.instances[inst].name,
                       self.instances[inst].x,
                       self.instances[inst].y,
                       self.instances[inst].z)

        return well_text

    def generate_sim_output_extract_files(self):
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


