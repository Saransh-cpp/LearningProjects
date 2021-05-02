j_max = float(input("Enter J max\n"))

v_max = float(input("Enter V max\n"))

j_sc = float(input("Enter J sc\n"))

v_oc = float(input("Enter V oc\n"))

fill_factor = (j_max*v_max) / (j_sc*v_oc)

print("Fill Factor =", fill_factor, "\n")

i_sc = float(input("Enter I sc\n"))

p_light = float(input("Enter P light\n"))

efficiency = (i_sc*fill_factor*v_oc) / p_light

print("Efficiency =", efficiency, "\n")


