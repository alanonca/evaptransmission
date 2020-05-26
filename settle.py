# T[C], RH[%], d0[um], cNaCl[mol/L]
# assuming:
# - droplet has constant temperature T

import math

def gettsettle_d2_epstein(T, RH, d0, cNaCl):
	# kholer size limit
	smallest_d = kohler_RT(RH, d0, cNaCl)
	


	
	return t_settle

def d2_law(T, RH, d0, cNaCl, t):
	# only works for >~mm size droplets
	# T[C], RH[%], d0[um], conc[mol/L], t[s]
	
	#constants specific to NaCl
	i = 2
	MWNaCl = 58.44 # [g/mol]

	T_K = T + 273.15
	D = D_water_air(T)
	M = 18.02e-3 # [kg/mol]
	rho1 = 1000 # [kg/m3]
	R = 8.3145 # [SI]
	d0_m = d0*1e-6 # [m]
	Zs = conc_to_molar_frac(cNaCl, MWNaCl)
	P = water_vapour_pressure(T)*1e5 # [Pa]

	# print(str(T_K)+'\n'+str(D)+'\n'+str(M)+'\n'+str(rho1)+'\n'+str(R)+'\n'+str(d0_m)+'\n'+str(Zs)+'\n'+str(P)+'\n'+str(RH))

	LHS = 1-8*D*M/rho1/R*((P*(1-i*Zs))/T_K-P/T_K*RH/100)*t/(d0_m)**2
	d = math.sqrt(LHS)*d0_m*1e6 # [um]
	return d # [um]


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

def kohler_RT(RH, d0, cSolute):
	# RH[%], d0[um], cSolulte[mol/L]
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

	return r_wet*2 # [um]

def sigma_w(TUnitC):
	# https://srd.nist.gov/JPCRD/jpcrd231.pdf
	# equation 1
	T = TUnitC + 273.15
	T_c = 647.15
	B = 235.8e-3
	b = -0.625
	mu = 1.256
	sigma = B*((T_c-T)/T_c)**mu*(1+b*(T_c-T)/T_c)
	return sigma

