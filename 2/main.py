import sys

def main():
	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()
	
	x = 0
	codesM = []
	for line in lines:
		s = line.split(",", -1)
		for e in s:
			try:
				codesM.append(int(e))
			except:
				pass

	#codesM[1] = 12
	#codesM[2] = 2

	for i in range(100):
		for j in range(100):
			codes = codesM.copy()
			codes[1] = i
			codes[2] = j
			idx = 0
			op = codes[0]

			while op != 99:
				idx1 = codes[idx+1]
				idx2 = codes[idx+2]
				idx3 = codes[idx+3]
				if op == 1:
					codes[idx3] = codes[idx1] + codes[idx2]
				if op == 2:
					codes[idx3] = codes[idx1] * codes[idx2]
				idx += 4
				op = codes[idx]

			if codes[0] == 19690720:
				print(str(100*i+j))
				return



if __name__== "__main__":
	main()
