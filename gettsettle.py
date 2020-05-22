# T[C], RH[fraction], d0[um], cNaCl[mol/L]



def gettsettle_d2_epstein(T, RH, d0, cNaCl):
	#Kohler equation

	#d^2 law
	
	return t_settle

def kohler(T, RT, cNaCl):
	# https://en.wikipedia.org/wiki/K%C3%B6hler_theory
	# All SI units
	M_w = 18.02e-3
	sigma_w = get_sigma_w(T)]
	rho_w = 1000

def get_sigma_w(TUnitC):
	# https://srd.nist.gov/JPCRD/jpcrd231.pdf
	# equation 1
	# T in K
	T = TUnitC + 273.15
	T_c = 647.15
	B = 235.8e-3
	b = -0.625
	mu = 1.256
	sigma = B*((T_c-T)/T_c)^mu*(1+b*(T_c-T)/T_c)
	return sigma

