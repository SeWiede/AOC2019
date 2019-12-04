import sys

def getDigit(n, i):
	if i == 0:
		return n % 10
	else:
		return ((int)(n//(10**i)))%10


def main():
	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()
	
	line = lines[0].split("-", -1)

	codes = []
	for e in line:
		codes.append(int(e))

	mc = 0
	for n in range(codes[0], codes[1]+1):
		double = False
		dec = True
		nodoubled = []
		doubled = []
		for i in range(2,6):
			poldd = getDigit(n, i-2)
			oldd = getDigit(n, i-1)
			d = getDigit(n, i)
			#print(d, oldd, poldd)
			if(oldd == poldd and oldd == d):
				if d in doubled and len(doubled) == 1:
					double = False
				nodoubled.append(d)
			if((not poldd in nodoubled) and poldd == oldd):
				double = True
				doubled.append(poldd)
			if((not oldd in nodoubled) and nodoubled != d and d == oldd):
				double = True
				doubled.append(d)
			if(poldd < oldd or oldd < d):
				dec = False
				break
		#print(nodoubled)	
		if double and dec:
			mc+=1
			

	print(mc)
	

if __name__== "__main__":
	main()
