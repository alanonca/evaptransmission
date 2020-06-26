import settle
import viability

# input T[C], RH[%], d0[um], cNaCl[mol/L], fall_height[m], model='empirical_small'
# default model selection of empirical model for droplet diameter <10um, also works for big droplet with ~40% error
# output settling time [hr]
t_stl = settle.settling_time(25,90,10,0.05,1.5)
print(t_stl)
print(type(t_stl))

# recommend to use model='empirical_big' if all droplets >10um
# doesn't quite work with small droplets with >150% error for <5um
t_stl2 = settle.settling_time(15,50,50,0.05,1.5,model='empirical_big')
print(t_stl2)

# input T[C], RH[%]
# output half life of virus [hr]
half_life = viability.half_life(25,90)
print(half_life) 
print(type(half_life))