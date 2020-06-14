# T[C], RH[%], d0[um], cNaCl[mol/L]
# assuming:
# - droplet has constant temperature T
# - dilute solution for kohler; any RH

import math
from scipy.interpolate import interp1d
import numpy as np

R = 8.3145

def settling_time(T, RH, d0, cNaCl):
	#Kohler size, epstein settling velocity
	r_eq = kohler(T, RH, d0, cNaCl)


	
	return t_settle

def kohler(T, RH, d0, cNaCl):
	# modified eq 8 from Lewis 2008; any RH instead of just h~1
	r_dry = r_dry_NaCl(d0, cNaCl)
	vw_bar = partial_molal_vol(T,cNaCl)/1e6 #m3/mol
	sigma = sigma_w(T)
	r_sigma_o = 2*vw_bar*sigma/(R*(T+273.15)) #m

	epsilon_sigma_o = r_sigma_o/r_dry

	c = 1.1 #for NaCl

	coeff = [math.log(RH/100), -epsilon_sigma_o, 0, c**3]
	epsilon_roots = np.roots(coeff)
	epsilon_root = epsilon_roots[~np.iscomplex(epsilon_roots)]
	epsilon = epsilon_root[0].real

	r_wet = r_dry*epsilon

	return r_wet

def r_dry_NaCl(d0, cNaCl):
	MWdry = 58.44
	rho_dry = 2.16 # [g/cm3]

	r0 = d0/2*1e-6 # [m]
	V0 = 4/3*math.pi*r0**3*1e3 # [L]
	ndry = cNaCl*V0 # [mol]
	mdry = ndry*MWdry # [g]
	r_dry = (3*mdry/(4*math.pi*rho_dry))**(1/3) # [cm]

	return r_dry/100 #m

def partial_molal_vol(T, cNaCl):
	# https://pubs.acs.org/doi/pdf/10.1021/j100697a022 eq 5 and table 2
	# https://pubs.acs.org/doi/pdf/10.1021/cr60229a001 eq 8 for Sv value in the prev ref
	# works for T between 0 and 55 C, need extrapolate functions to extend range

	T_Sv_arr = np.linspace(0, 70, num=15, endpoint=True)
	Sv_arr = np.array([1.444,1.529,1.613,1.697,1.782,1.868,1.955,2.046,2.138,2.234,2.333,2.435,2.542,2.653,2.768])
	f_Sv = interp1d(T_Sv_arr, Sv_arr)

	T_arr = np.array([0,5,15,25,35,45,55])
	v2o_arr = np.array([12.855, 14.175, 15.577, 16.624, 17.28, 17.592, 17.913])
	bvprime_arr = np.array([2.662, 1.341, 0.717, 0.079, -0.271, -0.519, -1.267])
	f_v2o = interp1d(T_arr, v2o_arr) #linear interpolation
	f_bvprime = interp1d(T_arr, bvprime_arr)

	v2 = f_v2o(T) + 1.5*f_Sv(T)*math.sqrt(cNaCl) + f_bvprime(T)*cNaCl #ml/mol
	return v2 #ml/mol

def viability(T,RH):
	#T[C], RH[%]
	#https://www.dhs.gov/science-and-technology/sars-calculator

	t_half = 29.98-0.58*T-0.12*RH #[hr]
	return t_half #half life[hr]


# def d2_law(T, RH, d0, cNaCl, t):
# 	# only works for >~mm size droplets
# 	# T[C], RH[%], d0[um], conc[mol/L], t[s]
	
# 	#constants specific to NaCl
# 	i = 2
# 	MWNaCl = 58.44 # [g/mol]

# 	T_K = T + 273.15
# 	D = D_water_air(T)
# 	M = 18.02e-3 # [kg/mol]
# 	rho1 = 1000 # [kg/m3]
# 	R = 8.3145 # [SI]
# 	d0_m = d0*1e-6 # [m]
# 	Zs = conc_to_molar_frac(cNaCl, MWNaCl)
# 	P = water_vapour_pressure(T)*1e5 # [Pa]

# 	# print(str(T_K)+'\n'+str(D)+'\n'+str(M)+'\n'+str(rho1)+'\n'+str(R)+'\n'+str(d0_m)+'\n'+str(Zs)+'\n'+str(P)+'\n'+str(RH))

# 	LHS = 1-8*D*M/rho1/R*((P*(1-i*Zs))/T_K-P/T_K*RH/100)*t/(d0_m)**2
# 	d = math.sqrt(LHS)*d0_m*1e6 # [um]
# 	smallest_d = kohler_RT(RH, d0, cNaCl)
# 	return max(d, smallest_d) # [um]


def water_vapour_pressure(T_C):
	# https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Mask=4
	# Stull, 1947
	T = T_C + 273.15
	A = 4.6543
	B = 1435.264
	C = -64.848
	P = 10**(A-(B/(T+C)))
	return P # [bar]

def conc_to_molar_frac(c, MWsolute, MWsolvent = 18.02, rho_solvent = 1):
	# c in mol/L, MW in g/mol, rho in kg/L
	#in 1 mol of solvent
	m_solvent = MWsolvent*1e-3 #[kg]
	V_solvent = m_solvent/rho_solvent #[L]
	n_solute = V_solvent*c # [mol]
	x = n_solute/(1+n_solute)
	return x

def D_water_air(T):
	# T in C
	# https://www.researchgate.net/post/Binary_diffusion_coefficients_for_water_vapour_in_air_at_normal_pressure
	D = 22.5e-6*((T+273.15)/273.15)**1.8
	return D # [m2/s] water vapour in air

# def kohler_RT(RH, d0, cSolute):
# 	# RH[%], d0[um], cSolulte[mol/L]
# 	# Lewis 2008
# 	# Kelvin effect neglible i.e big droplets
# 	# return equilibrium droplet diameter in um for the given amount of salt

# 	# empirical values for NaCl
# 	a = 1.08
# 	b = 1.1
# 	MWdry = 58.44
# 	rho_dry = 2.16 # [g/cm3]

# 	h = min(RH/100, 0.999) # avoid h=1 case for epsilon calc
# 	epsilon = a * (b + 1/(1-h))**(1/3)
# 	# print('epsilon is ' + str(epsilon))

# 	r0 = d0/2*1e-6 # [m]
# 	V0 = 4/3*math.pi*r0**3*1e3 # [L]
# 	ndry = cSolute*V0 # [mol]
# 	mdry = ndry*MWdry # [g]
# 	r_dry = (3*mdry/(4*math.pi*rho_dry))**(1/3) # [cm]

# 	r_wet = r_dry*epsilon*1000 # [um]

# 	return r_wet*2 # [um]

def sigma_w(TUnitC):
	# https://srd.nist.gov/JPCRD/jpcrd231.pdf
	# equation 1
	T = TUnitC + 273.15
	T_c = 647.15
	B = 235.8e-3
	b = -0.625
	mu = 1.256
	sigma = B*((T_c-T)/T_c)**mu*(1+b*(T_c-T)/T_c)
	return sigma #N/m

