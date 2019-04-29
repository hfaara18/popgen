import random
import os
import math
import re

class Pop_Query:
    def __init__(self, name):
        self.filename = name
        self.names = ["ZPVE", "H", "S", "G", "delG", "Ni", "N", "populations"]
        self.command = "freqchk"

        _filename = name.rfind("/")
        filename_ = name.rfind(".chk")
        self.prefix = name[_filename + 1 : filename_]
        self.output = ""


    def get_params(self):
        # hyper_chem = str(input("Write HyperChem file? ")) + " "
    	hyper_chem = "N "

    	temp = str(input("Give temperature in K: ")) + " "

    	#scale = str(input("Scale factor: ")) + " "
    	scale = "1 "

    	pressure = str(input("Give pressure in atm: ")) + " "
    	# pressure = "1 "

    	masses = str(input("Use Principal Masses? ")) + " "
    	project = "N "

    	#project = str(input("Project? ")) + " "
    	# output = str(">> " + input("Output file: "))

    	self.output = str(">> " + str(self.prefix) + ".txt")

    	return self.command, self.prefix, hyper_chem, temp, scale, pressure, masses, project, self.output

    def get_values(self):
        zpve_pattern = re.compile(r"\s+(\d+.\d+)\s+\(Kcal/Mol\)")
        total_pattern = re.compile(r"\s+Total\s+(\d+.\d+)\s+(\d+.\d+)\s+(\d+.\d+)")

        with open(self.filename) as file:
            line = file.readline();
            while line != "":
                if "(Kcal/Mol)" in line:
                    zpve_matches = re.finditer(zpve, line)
                    zpve = float(zpve_matches.group(1))

                if "Total" in line:
                    total_matches = re.finditer(total, line)
                    enthalpy = float(total_matches.group(1))
                    entropy = float(total_matches.group(3))/1000


        G = enthalpy - 4* entropy
        delG = 0
        Ni = exp(-0/4/0.0019872)
        N = Ni
        Pop = str((Ni/ N) * 100) + "%"

        return float(zpve), float(enthalpy), float(entropy), float(G), float(delG), float(Ni), float(N), Pop

    def create_spreadsheet(self):
        print("fghfj")

def main():
    Q = Pop_Query("dmtar_32.chk")
    params = Q.get_params()
    os.system(" ".join(params))
    print(Q.get_values())

if __name__ == '__main__':
    main()
