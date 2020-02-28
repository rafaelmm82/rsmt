# rsmt
Reservoir Surrogate Modeling Toolbox (rsmt), is a data-driven surrogate modeling 
package and related tools focused on speed and easiness way to create  initial 
model propositions in the proxy/surrogate/substitute problem domain for
oil and gas reservoirs.


### simhandle

Simulation Handle, is the module responsible to dealing with the specifications
of the oil and gas reservoir simulations. For now, only working with CMG v.2015.

It is based on the following classes:
 - Reservoir, responsible to characterize the volume (cartesian only), specially
 its static properties like porosity (i, j, k) and permeability.
 - Instance, is related to one simulation run of a reservoir considering its
 individual development plan.
 - Project, consist in aggregate a set of reservoir development simulations,
 considering its individual plan, sharing the same time step.
 - Plan, a development specification considering the well configuration, types,
 opens, closeness, over the time steps. (FUTURE)

**Doc Description:** 
"The simhandle module is responsible to interact with the oil and gas reservoir 
simulator. Through it, it is possible to define a generic reservoir 
specification (dimension, actual state, and petrophysical properties), a set of 
wells and its attributes and a plan of development (duration, step size, etc.). 
With that, it is possible to generate the reservoir simulator inputs, manage the 
execution process, retrieve the output and incorporate it. With all this data 
the module is able to feed the Data Source storage container (data and 
metadata).
"

### datahandle


### mlmodel


### modelsim


### report


### visualization


### datamanager