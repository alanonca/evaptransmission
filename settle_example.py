import settle
import viability

# T[C], RH[%], d0[um], cNaCl[mol/L], fall_height[m]; output settling time [hr]
t_stl = settle.settling_time(25,90,10,0.05,1.5)
print(t_stl)
print(type(t_stl))

# T[C], RH[%]; output half life of virus [hr]
half_life = viability.half_life(25,90)
print(half_life) 
print(type(half_life))