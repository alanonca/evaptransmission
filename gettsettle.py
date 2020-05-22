# T[C], RH[%], d0[um], cNaCl[mol/L]

import math

def gettsettle_d2_epstein(T, RH, d0, cNaCl):
	smallest_d = kohler_RT(RH, d0, cNaCl)

	#d^2 law
	
	return t_settle

def kohler_RT(RH, d0, cSolute):
	# Lewis 2008
	# Kelvin effect neglible i.e big droplets
	# return equilibrium droplet diameter in um for the given amount of salt

	# empirical values for NaCl
	a = 1.08
	b = 1.1
	MWdry = 58.44
	rho_dry = 2.16 # [g/cm3]

	h = min(RH/100, 0.999) # avoid h=1 case for epsilon calc
	epsilon = a * (b + 1/(1-h))**(1/3)
	# print('epsilon is ' + str(epsilon))

	r0 = d0/2*1e-6 # [m]
	V0 = 4/3*math.pi*r0**3*1e3 # [L]
	ndry = cSolute*V0 # [mol]
	mdry = ndry*MWdry # [g]
	r_dry = (3*mdry/(4*math.pi*rho_dry))**(1/3) # [cm]

	r_wet = r_dry*epsilon*1000 # [um]

	return r_wet*2

def get_sigma_w(TUnitC):
	# https://srd.nist.gov/JPCRD/jpcrd231.pdf
	# equation 1
	# T in K
	T = TUnitC + 273.15
	T_c = 647.15
	B = 235.8e-3
	b = -0.625
	mu = 1.256
	sigma = B*((T_c-T)/T_c)**mu*(1+b*(T_c-T)/T_c)
	return sigma

