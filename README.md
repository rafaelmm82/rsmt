# rsmt
Rapid Surrogate Modeling Toolbox (rsmt), is a data-driven surrogate modeling 
package and related tools focused on speed and easiness to create some 
initial model propositions in the proxy/surrogate/substitute problem domain.


### simhand

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
 opens, closeness, over the time steps.
