def half_life(T,RH):
	#T[C], RH[%]
	#https://www.dhs.gov/science-and-technology/sars-calculator

	t_half = 29.98-0.58*T-0.12*RH #[hr]
	return t_half #half life[hr]