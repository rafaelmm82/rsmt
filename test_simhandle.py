from rsmt.simhandle import Manager, ReservoirCartesian, SimProject, Well


work_dir = '/home/rafael/GitHub/rsmt/test_sim'

# setup
#  reservoir
#  wells
#  project
#  manager

manager = Manager(work_dir=work_dir)

reservoir = ReservoirCartesian(name='spe9',
                               dimension=[24, 25, 15],
                               file_header='spe9_header.dat')

wells_pos = {
    'Producer1': [5, 1],
    'Producer2': [8, 2],
    'Producer3': [11, 3],
    'Producer4': [10, 4],
    'Producer5': [12, 5],
    'Producer6': [4, 6],
    'Producer7': [8, 7],
    'Producer8': [14, 8],
    'Producer9': [11, 9],
    'Producer10': [12, 10],
    'Producer11': [10, 11],
    'Producer12': [5, 12],
    'Producer14': [11, 14],
    'Producer15': [13, 15],
    'Producer16': [15, 16],
    'Producer17': [11, 17],
    'Producer18': [12, 18],
    'Producer19': [5, 19],
    'Producer20': [8, 20],
    'Producer21': [11, 21],
    'Producer22': [15, 22],
    'Producer23': [12, 23],
    'Producer24': [10, 24],
    'Producer25': [17, 25],
}

# initially fixed z position for perforation
z_pos = 3
wells = [Well(name=k, x=v[0], y=v[1], z=z_pos) for k, v in wells_pos.items()]

steps = list(range(1, 365, 30))

project = SimProject(name='onewell_z3', reservoir=reservoir,
                     instances=wells, time_steps=steps)


manager.setup(reservoir, project, wells)


# %%
# generate files

print(manager.reservoir.header)
print(manager.project.generate_time_steps())
print(manager.project.generate_well_header())
print(manager.project.generate_well_entry(1))

manager.generate_files()
# execute plans

# retrieve data

