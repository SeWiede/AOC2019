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
		for i in range(1,6):
			oldd = getDigit(n, i-1)
			d = getDigit(n, i)
			if(oldd == d):
				double = True
			if(oldd < d):
				dec = False
				break		
		if double and dec:
			mc+=1
			

	print(mc)
	

if __name__== "__main__":
	main()
