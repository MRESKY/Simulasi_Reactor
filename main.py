from reactor import Reactor
from kinetic_model import kineticModel
from controller import controlSystem

volume = 1000  # dalam liters
temperature = 300  # dalam Kelvin
pressure = 101325  # dalam Pascals
reactant_concentration = 1.0  # dalam mol/L
reaction_rate_constant = 0.05  # dalam L/(mol*s)
reaction_order = 1  # first-order reaksi
simulation_steps = 10  # banyaknya iterasi simulasi


reactor = Reactor(volume, temperature, pressure, reactant_concentration)
kinetic_model = kineticModel(reactor, reaction_rate_constant, reaction_order)
controller = controlSystem(reactor, kinetic_model)
controller.run_simulation(simulation_steps)
