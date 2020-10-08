import settle

# input T[C], RH[%], d0[um], cNaCl[mol/L], fall_height[m], model='sc'
# default model selection of stokes cunningham
# output settling time [hr]
t_stl = settle.settling_time(25,90,10,0.08,1.5,'sc')
print(t_stl)
print(type(t_stl))

# model parameter takes other arguments
t_stl = settle.settling_time(25,90,10,0.08,1.5,'epstein')
print(t_stl)
print(type(t_stl))

# get Knudsen number of air
for T in [273, 278, 283, 288, 293, 298, 303, 308, 313]:
	print(settle.Kn_atm_air(T))