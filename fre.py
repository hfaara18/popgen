import random
import os
import xlsxwriter
from math import *

# output1 = ""
#filename = int(random.random() * 100000)
filename = ""
names = ["ZPVE", "H", "S", "G", "delG", "Ni", "N", "populations"]


def get_params():
	#import random

	command = "freqchk "
	file = str(input("Give file directory: ")) + " "
	#hyper_chem = str(input("Write HyperChem file? ")) + " "

	filename = getFilename(file)
	#print(filename)

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


def getValues(name):

	#import random
	#filename = str(int(random.random() * 10000)) + ".txt"
	#output = open(filename, "w+")
	#input = open(str(input("Input file: ")))

	#print(filename);

	output = str(name) + ".txt"
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

			#print(enthalpy)
			#print(ind3)
			#print(entropy)

		if kcalPerMol in line:
			ind6 = line.index(kcalPerMol)
			ind5 = line.index(zpve_space) + 1

			zpve = line[ind5 + len(zpve_space) :ind6]

			#print(line)
			#print(zpve)

	input.close()

	G = float(enthalpy) - 4* float(entropy)/1000
	delG = 0
	Ni = exp(-0/4/0.0019872)
	N = Ni
	Pop = str((Ni/ N) * 100) + "%"

	return float(zpve), float(enthalpy), float(entropy)/1000, float(G), float(delG), float(Ni), float(N), Pop

def getFilename(name):

	_filename = name.rfind("/");
	filename_ = name.rfind(".chk");
	filename = name[_filename + 1:filename_]
	return filename;

def createSpreadsheet(name):
	#values = []
	values = list(getValues(name))
	values.append(values[1] - 4*values[2])

	row = 2
	col = 1

	workbook = xlsxwriter.Workbook(str(name) + ".xlsx")
	worksheet = workbook.add_worksheet()

	bold = workbook.add_format({"bold" : True})
	worksheet.set_column("B:B", 15)
	worksheet.set_column("C:C", 12)

	worksheet.write(0, 0, str(name), bold)


	for index, item in enumerate(names):
		worksheet.write(row, col, item, bold)

		if index < len(values):
			worksheet.write(row, col +1, values[index])

		row += 1

	workbook.close()


if __name__=="__main__":

	params = get_params();

	name = getFilename("".join(params))

	os.system("".join(params))

	getValues(name)
	createSpreadsheet(name)
	#os.system(get_params())
