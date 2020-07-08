import viability

# input T[C], RH[%]
# output half life of virus [hr]
half_life = viability.half_life_surface(25,90)
print(half_life) 
print(type(half_life))

# input T[C], RH[%], UVB[W/m2]
# output decay rate of virus [min-1]
# ln2/k gives half life in minutes if desired
# tested range T=10-30C, RH=20-70%, UVB=0-1.9 W/m2
decay_rate = viability.kdecay(10,30,0)
print(decay_rate) 
print(type(decay_rate))