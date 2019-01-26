

def getValues() {

	import random

	filename = str(int(random.random() * 10000)) + ".txt"

	#output = open(filename, "w+")

	input = open(str(input("Input file: ")))

	intro = "Total                  " 
	end_to_cv = "              "
	enthalpy = 0
	entropy = 0
	cv = 0
	cv_to_entropy = "             "

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




}
