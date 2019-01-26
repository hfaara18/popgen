from subprocess import Popen, PIPE
import os

#	//os.system("freqchk >> new.txt")


with Popen(["cmd", "python"], stdin=PIPE, stdout=PIPE, universal_newlines=True) as p:
	print("freqchk")
	p.stdin.flush()

	for line in p.stdout:
		if line.startswith("Checkpoint file"):
			answer = "gaussian/dmtar_4.chk"
			print(line)
		elif line.startswith("Write Hyperchem files"):
			answer = "N"
		elif line.startswith("Temperature"):
			# filename = get_filename_from_prompt(line) # a regex could be used
			answer = 4
		elif line.startswith("Pressure"):
			answer = 1
		elif line.startswith("Scale factor for frequencies during thermochemistry"):
			answer = 1
		elif line.startswith("Do you want to use the principal isotope mass number"):
			answer = "Y"
		else:
			continue # skip it
		print(answer, file=p.stdin) # provide answer
		p.stdin.flush()
