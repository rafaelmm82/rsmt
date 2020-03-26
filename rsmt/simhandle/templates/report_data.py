report_header = """

*FILE '{filename_irf}'

"""

report_static_properties = """
** 
** static properties
** -----------------
** 

*OUTPUT 'static_data/{reservoir_name}_permeability_i.rwo'
*PROPERTY-FOR 'Permeability I'              0 *MATRIX *XYZLAYER 0
*OUTPUT 'static_data/{reservoir_name}_permeability_j.rwo'
*PROPERTY-FOR 'Permeability J'              0 *MATRIX *XYZLAYER 0
*OUTPUT 'static_data/{reservoir_name}_permeability_k.rwo'
*PROPERTY-FOR 'Permeability K'              0 *MATRIX *XYZLAYER 0
*OUTPUT 'static_data/{reservoir_name}_porosity.rwo'
*PROPERTY-FOR 'Porosity'              0 *MATRIX *XYZLAYER 0

"""

report_dynamic_data_header = """
** 
** dynamic properties
** ------------------
** 

"""

report_dynamic_data = """
*OUTPUT   'dynamic_data/{sim_name}_{property_min}_step_{step0}.rwo'
*PROPERTY-FOR '{property_imex}'              {step} *MATRIX *XYZLAYER 0
"""


report_well_header = """
** 
** dynamic properties
** ------------------
** 
*LINES-PER-PAGE 5000
*TIMES-FOR {list_of_steps}

"""

report_well_entry = """
*OUTPUT '{sim_name}_{well_name}_cumulative_production.rwo'
*TABLE-FOR
   *COLUMN-FOR   *WELLS   '{well_name}'
      *PARAMETERS   'Cumulative Oil SC' 
      *PARAMETERS   'Cumulative Water SC'
      *PARAMETERS   'Cumulative Gas SC'
*TABLE-END

"""
