def half_life_surface(T,RH):
	#T[C], RH[%]
	#https://www.dhs.gov/science-and-technology/sars-calculator

	t_half = 29.98-0.58*T-0.12*RH #[hr]
	return t_half #half life[hr]

def kdecay(T, RH, UVB):
	# T[C], RH[%], UVB[W/m2]
	# regression model from Paul D, DHS

	A = 7.56923717497566
	B = 1.4112551882451
	T_norm = (T-20.54)/10.66
	C = 0.0217570346639
	RH_norm = (RH-45.235)/28.665
	D = 7.5527229297008
	UVB_norm = (UVB-50)/50
	E = 1.3973422174602

	# print(A)
	# print(B*T_norm)
	# print(C*RH_norm)
	# print(D*UVB_norm)
	# print(T_norm*UVB_norm)

	k = A + B*T_norm + C*RH_norm + D*UVB_norm + E*T_norm*UVB_norm
	return max(0,k)