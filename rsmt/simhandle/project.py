

class Project:

    def __init__(self, name=None, reservoir=None, wells=None,
                 simulations=None, time_steps=None):

        # initially each run has only one producer well
        self.name = name
        self.reservoir = reservoir
        self.wells = wells
        self.simulations = simulations  # array of simulations instances
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

    def generate_sim_output_extract_file(self, inst):

        output = ""

        # filename
        output += "\n*FILE '{}_{}_{}.irf".format(self.reservoir.name,
                                                 self.name,
                                                 self.instances[inst-1].name)

        # static content
        output += "\n**\n** static properties\n**\n\n"
        output += """
*OUTPUT 'static/sim_{}_permeability_i.rwo'
*PROPERTY-FOR 'Permeability I'              0 *MATRIX *XYZLAYER 0
*OUTPUT 'static/sim_{}_permeability_j.rwo'
*PROPERTY-FOR 'Permeability J'              0 *MATRIX *XYZLAYER 0
*OUTPUT 'static/sim_{}_permeability_k.rwo'
*PROPERTY-FOR 'Permeability K'              0 *MATRIX *XYZLAYER 0
*OUTPUT 'static/sim_{}_porosity.rwo'
*PROPERTY-FOR 'Porosity'              0 *MATRIX *XYZLAYER 0
\n\n
""".format(inst, inst, inst, inst)

        # dynamic content
        output += "\n**\n** dynamic properties\n**\n"

        # oil saturation
        for t in self.time_steps:
            output += "\n*OUTPUT   'oil_saturation/sim_{}_oil_saturation_time_{}.rwo'".format(inst, t)
            output += "\n*PROPERTY-FOR 'Oil Saturation'              {} *MATRIX *XYZLAYER 0".format(t)
        output += '\n\n'

        # gas saturation
        for t in self.time_steps:
            output += "\n*OUTPUT   'gas_saturation/sim_{}_gas_saturation_time_{}.rwo'".format(inst, t)
            output += "\n*PROPERTY-FOR 'Gas Saturation'              {} *MATRIX *XYZLAYER 0".format(t)
        output += '\n\n'

        # water saturation
        for t in self.time_steps:
            output += "\n*OUTPUT   'water_saturation/sim_{}_water_saturation_time_{}.rwo'".format(inst, t)
            output += "\n*PROPERTY-FOR 'Water Saturation'              {} *MATRIX *XYZLAYER 0".format(t)
        output += '\n\n'

        # pressure
        for t in self.time_steps:
            output += "\n*OUTPUT   'pressure/sim_{}_pressure_time_{}.rwo'".format(inst, t)
            output += "\n*PROPERTY-FOR 'Pressure'              {} *MATRIX *XYZLAYER 0".format(t)
        output += '\n\n'

        # production
        output += "\n**\n** production\n**\n\n"

        output += "\n*OUTPUT 'sim_{}_cumulative_production.rwo'".format(inst)

        output += "\n*TIMES-FOR"
        for t in self.time_steps:
            output += " {}".format(t)
        output += "\n*LINES-PER-PAGE 5000"
        output += "\n*TABLE-FOR"
        output += "\n   *COLUMN-FOR   *WELLS   '{}'".format(self.instances[inst-1].name)
        output += "\n      *PARAMETERS   'Cumulative Oil SC'"
        output += "\n      *PARAMETERS   'Cumulative Water SC'"
        output += "\n      *PARAMETERS   'Cumulative Gas SC'"
        output += "\n*TABLE-END"

        return output

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


class Simulation:

    def __init__(self, name=None, wells=None):
        self.name = name
        self.wells = wells  # an array of Well objects

