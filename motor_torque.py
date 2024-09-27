"""Code for calculating the maximum torque to rotate the panel"""

import math as mt

# Initialize parameters

r = 2.5 * .254  # Radius of tube [m]
rho_air = 1.225  # Density of air [kg/m^3]
G_cp = .5  # Coefficient of drag
A = 1 * 2  # Area of panel [m^2]
v = 9  # Airspeed [m/s]
P_snow = 250  # Snow load [N/m^2]
mu_tube = .25  # Coefficient of friction on tube
z = .15  # Distance from center of rotation to panel CG
theta = 60  # Angle of panel
gear_ratio = 1 / 10  # Gear ratio of gearbox

# Calculate Forces

F_aero = 0.5 * rho_air * (v ** 2) * G_cp * A  # Aerodynamic force on panel [N]
F_snow = P_snow * A  # Force from snow load [N]
F_friction = mu_tube * F_snow  # Frictional budging force [N]

# Calculate Moment Arms for Snow and Aero Forces

x = z * mt.cos(mt.radians(theta))  # Snow moment arm [m]
y = z * mt.sin(mt.radians(theta))  # Aero moment arm [m]

# Calculate Torques

T_snow = F_snow * x  # Torque from snow load [N*m]
T_aero = F_aero * y  # Torque from wind load [N*m]
T_f = F_friction * r  # Torque from friction

T_total = T_snow + T_aero + T_f  # Total torque on gearbox

T_motor = T_total * gear_ratio  # Torque motor sees

"""Section for printing results"""

print('\nThe maximum torque the motor sees is ' + str(round(T_motor, 3)) + str(' [N]'))

print('\nForces:\n')
print('Aero Force is = ' + str(round(F_aero, 3)) + str(' [N]'))
print('Snow Force = ' + str(round(F_snow, 3)) + str(' [N]'))

print('\nMoment Arms\n')
print('x = ' + str(round(x, 3)) + str(' [m]'))
print('y = ' + str(round(y, 3)) + str(' [m]'))

print('\nTorques\n')
print('T_snow = ' + str(round(T_snow, 3)) + str(' [N*m]'))
print('T_snow = ' + str(round(T_aero, 3)) + str(' [N*m]'))
print('T_f = ' + str(round(T_f, 3)) + str(' [N*m]'))
print('T_total = ' + str(round(T_total, 3)) + str(' [N*m]'))
print('T_motor = ' + str(round(T_motor, 3)) + str(' [N*m]'))


#Test Change