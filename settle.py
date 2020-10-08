# T[C], RH[%], d0[um], cNaCl[mol/L], fall_height[m] unless otherwise stated
# assuming:
# - droplet has constant temperature T
# - dilute solution for kohler; any RH

import math
from scipy.interpolate import interp1d
import numpy as np

R = 8.3145

def settling_time(T, RH, d0, cNaCl, fall_height, model='sc'):
	r_eq = kohler(T, RH, d0, cNaCl) #m
	# print('size =' + str(r_eq*2*1e6))
	# print('kholer size in nm=' + str(r_eq*1e9))

	# get rho_p after evaporation [kg/m3]
	totalV = 4/3*math.pi*r_eq**3
	V_NaCl = 4/3*math.pi*r_dry_NaCl(d0, cNaCl)**3
	m_H2O = (totalV - V_NaCl) * 1000
	m_NaCl = V_NaCl * 2160
	totalm = m_NaCl+m_H2O
	rho_p = get_rho_p_recur(m_NaCl, totalm, totalV, T) #recursion to get rho_p

	# both empirical models assume 1.8g/cm3 density
	if model == 'empirical_small':
		settle_v = empirical_small_v(r_eq*2*1e6)/1e3 #m/s
	elif model == 'empirical_big':
		settle_v = empirical_big_v(r_eq*2*1e6)/1e3 #m/s
	elif model == 'epstein':
		settle_v = epstein_v(T, r_eq, rho_p) #m/s
	elif model == 'sc':
		settle_v = stokes_cunningham(T+273.15, r_eq*2, rho_p)
	else:
		print('invalid model selection in settling_time param input')

	# print('settle_v=' + str(settle_v*1000/3600))

	settle_t = fall_height/settle_v #s

	return settle_t/3600 #hr

def get_rho_p_recur(m_NaCl, totalm, totalV, T):
	NaCl_wtperc = m_NaCl / totalm
	rho_p = rho_NaCl_soln(T+273.15, NaCl_wtperc)
	err = abs(rho_p / (totalm/totalV) - 1)
	# print(err)

	if err>0.001: #if error larger than 0.1%
		totalm = totalV * rho_p
		rho_p = get_rho_p_recur(m_NaCl, totalm, totalV, T)

	return rho_p

def stokes_cunningham(T, Dp, rho_p):
	# temperature in K, particle diametre in m, density of particle in kg/m3 (all SI units)
	
	mu_air = 1.81e-5 # SI unit
	g = 9.8

	v_terminal = rho_p*Dp**2*g/(18*mu_air)

	# apply cunningham if Re < 1
	Re = Re_atm(rho_p, v_terminal, Dp)
	if Re < 1:
		Kn = Kn_atm_p(T, Dp)
		correctionFactor = 1 + 2.52*Kn
		v_terminal = v_terminal * correctionFactor

	return v_terminal

def Re_atm(rho_p, v, Dp):
	# density of particle, velocity, particle diametre in SI units
	# in air

	mu_air = 1.81e-5 # SI unit
	Re = rho_p*v*Dp/mu_air
	return Re

def Kn_atm_p(T, Dp):
	# T in K, Dp in m
	# for air in atmospheric pressure

	NoverV = 101325/8.3145/T*6.022e23 #molecules per volume
	meanFreePath = 1/(math.sqrt(2)*math.pi*(3.1e-10)**2*NoverV) 

	return meanFreePath/Dp

def Kn_atm_air(T):
	# T in K
	# for air in atmospheric pressure

	NoverV = 101325/8.3145/T*6.022e23 #molecules per volume
	meanFreePath = 1/(math.sqrt(2)*math.pi*(3.1e-10)**2*NoverV) 

	return meanFreePath/3.1e-10

def rho_NaCl_soln(T, wtperc):
	# T in K, wtperc in weight percent concentration
	# https://www.researchgate.net/publication/280063894_Mathematical_modelling_of_density_and_viscosity_of_NaCl_aqueous_solutions
	A1 = 750.2834 + 26.7822*wtperc - 0.26389*wtperc**2
	A2 = 1.90165 - 0.11734*wtperc + 0.00175*wtperc**2
	A3 = -0.003604 + 0.0001701*wtperc - 0.00000261*wtperc**2
	rho = A1 + A2*T + A3*T**2
	return rho

def empirical_small_v(d):
	# input diameter in um, output U in mm/s
	# for big droplets
	# data from Jakobsen 2019
	U = 0.0077*d**2 - 0.0256 * d + 0.0405
	return U

def empirical_big_v(d):
	# input diameter in um, output U in mm/s
	# for small droplets
	U = 0.0131*d**2 - 0.0746 * d + 0.1123
	return U

def epstein_v(T, r, rho_p):
	# [C] and [m], and [kg/m3]
	# Jakobsen 2019 equation 7
	# atmospheric pressure
	# k = 1.38064852e-23
	# N_A = 6.02214086e23
	P = 101325 #[Pa]
	g = 9.8
	R = 8.3145
	MW_air = 28.9647e3
	c_bar = math.sqrt(8*R*(T+273.15)/(math.pi*MW_air))

	delta = 1.18 # Jakobsen 2019 table 2 and fig 4, can be imporoved as f(size)
	rho_air = P*MW_air*1e-3/(R*(T+273.15)) #ideal gas law, constant P, [kg/m3]

	U = rho_p*g*r/(rho_air*c_bar*delta) #m/s

	return U

def kohler(T, RH, d0, cNaCl):
	# modified eq 8 from Lewis 2008; any RH instead of just h~1
	# results verified to Lewis 2008 Fig 2
	r_dry = r_dry_NaCl(d0, cNaCl) #m

	# print('r_dry in nm' + str(r_dry*1e9))

	vw_bar = partial_molal_vol(T,cNaCl)/1e6 #m3/mol
	sigma = sigma_w(T)
	r_sigma_o = 2*vw_bar*sigma/(R*(T+273.15)) #m

	epsilon_sigma_o = r_sigma_o/r_dry

	c = 1.1 #for NaCl

	coeff = [math.log(RH/100), -epsilon_sigma_o, 0, c**3]
	# coeff = [-(1-RH/100), -epsilon_sigma_o, 0, c**3]
	epsilon_roots = np.roots(coeff)
	epsilon_root = epsilon_roots[~np.iscomplex(epsilon_roots)]
	epsilon = epsilon_root[0].real.item() #item function converts numpy.float to float

	# print(coeff)
	# print(epsilon_roots)
	# print(epsilon_root)
	# print(epsilon)

	r_wet = r_dry*epsilon

	return r_wet #m

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

