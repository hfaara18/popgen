import random

# output1 = ""
filename = int(random.random() * 100000)


def get_params():
	#import random
	
	
	command = "freqchk " 
	file = str(input("Give file directory: ")) + " "
	#hyper_chem = str(input("Write HyperChem file? ")) + " "
	
	hyper_chem = "N "
	temp = str(input("Give temperature in K: ")) + " "
	
	#scale = str(input("Scale factor: ")) + " "
	scale = "1 "
	
	#pressure = str(input("Give pressure in atm: ")) + " "
	pressure = "1 "
	
	masses = str(input("Use Principal Masses? ")) + " "
	project = "N "
	
	#project = str(input("Project? ")) + " "
	# output = str(">> " + input("Output file: "))
	
	output = str(">> " + str(filename) + ".txt")
	
	
	return command, file, hyper_chem, temp, scale, pressure, masses, project, output
	
	


def getValues():

	#import random
	#filename = str(int(random.random() * 10000)) + ".txt"
	#output = open(filename, "w+")
	#input = open(str(input("Input file: ")))
	
	
	output = str(filename) + ".txt"
	
	input = open(output, "r+")
	input.seek(0)

	intro = "Total                  " 
	end_to_cv = "              "
	enthalpy = 0
	entropy = 0
	cv = 0
	cv_to_entropy = "             "
	kcalPerMol = " (Kcal/Mol)"
	zpve_space = "                                 "
	zpve = 0

	for line in input:
		if intro in line:
			ind1 = line.index(intro)
			ind2 = line.index(end_to_cv, ind1 + len(intro))
			enthalpy = line[ind1 + len(intro): ind2]
			
			#line.index(enthalpy)
			
			ind3 = line.index(cv_to_entropy, ind2 +1)
			ind4 = line.index(cv_to_entropy, ind3+ len(cv_to_entropy))
			
			#ind4 = line.index(ind3,
			#cv = line[ind4 + len(cv_to_entropy):
			
			
			entropy = line[ind4 + len(cv_to_entropy):]
			
			print(enthalpy)
			#print(ind3)
			print(entropy)
			
		if kcalPerMol in line:
			ind6 = line.index(kcalPerMol)
			ind5 = line.index(zpve_space) + 1
			
			
			zpve = line[ind5 + len(zpve_space) :ind6]
			
			#print(line)
			print(zpve)
			
			
			
if __name__ == "__main__":

	import os
	
	os.system("".join(get_params()))
	
	getValues()
	#os.system(get_params())
	


