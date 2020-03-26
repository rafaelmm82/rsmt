from rsmt.simhandle import Manager, ReservoirCartesian, VerticalWell
from rsmt.simhandle import Project, Simulation

work_dir = 'C:\\Users\\magalraf\\Documents\\GitHub\\rsmt\\test_sim'

# %%

reservoir = ReservoirCartesian(name='spe9', dimension=[24, 25, 15], template='spe9')

z = 3
well_descriptions = {
    'prod_01': [5, 1, z],
    'prod_03': [11, 3, z],
    'prod_05': [12, 5, z],
    'prod_09': [11, 9, z],
    'prod_10': [12, 10, z],
    'prod_17': [11, 17, z],
    'prod_18': [12, 18, z],
    'prod_19': [5, 19, z],
    'prod_24': [10, 24, z],
    'prod_25': [17, 25, z],
}

well_list = [VerticalWell(name=k, x=v[0], y=v[1], z=v[2])
             for k, v in well_descriptions.items()]

simulations = [Simulation(name=str(e), wells=[w])
               for e, w in enumerate(well_list)]

monthly_10_years = list(range(1, 3650, 30))

project_DNN = Project(name='spe9_one_well_z3',
                      reservoir=reservoir,
                      wells=well_list,
                      simulations=simulations,
                      time_steps=monthly_10_years)

manager = Manager(work_dir=work_dir, project=project_DNN)


# %%
manager.setup_simulation()

# %%
# generate files

print(manager.reservoir.header)
print(manager.project.generate_time_steps())
print(manager.project.generate_well_header())
print(manager.project.generate_well_entry(1))

manager.generate_files()
print(manager.project.generate_sim_output_extract_file(2))

# execute plans

# retrieve data

