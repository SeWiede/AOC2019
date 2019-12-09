import sys

def main():
	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()
	
	x = 0
	codes = []
	for line in lines:
		s = line.split(",", -1)
		for e in s:
			try:
				codes.append(int(e))
			except:
				pass

	memory = []
	idx = 0
	while True:
		op =codes[idx]%100 #is 0x anyway
		if op == 99:
			break
		C = codes[idx]/100%10
		B = codes[idx]/1000%10
		A = codes[idx]/10000%10
		idx1 = codes[idx+1]
		idx2 = codes[idx+2]
		idx3 = codes[idx+3]
		
		if op == 1:	
			rd = idx1 if C!=0 else codes[idx1]
			rt = idx2 if B!=0 else codes[idx2]
			rs = rd + rt
			codes[idx3] = rs
			idx += 4
		if op == 2:
			rd = idx1 if C!=0 else codes[idx1]
			rt = idx2 if B!=0 else codes[idx2]
			rs = rd * rt
			codes[idx3] = rs
			idx += 4
		if op == 3:
			i = sys.stdin.readline()
			try:
				codes[idx1] = int(i)
			except:
				codes[idx1] = i
				print >> sys.stderr, "god damnit"
			idx += 2
		if op == 4:
			print(codes[idx1])
			idx += 2
		if op == 5:
			rd = idx1 if C!=0 else codes[idx1]
			rt = idx2 if B!=0 else codes[idx2]
			idx = rt if rd else idx+3
		if op == 6:
			rd = idx1 if C!=0 else codes[idx1]
			rt = idx2 if B!=0 else codes[idx2]
			idx = rt if not rd else idx+3
		if op == 7:			
			rd = idx1 if C!=0 else codes[idx1]
			rt = idx2 if B!=0 else codes[idx2]
			codes[idx3] = 1 if rd < rt else 0
			idx += 4
		if op == 8:			
			rd = idx1 if C!=0 else codes[idx1]
			rt = idx2 if B!=0 else codes[idx2]
			codes[idx3] = 1 if rd == rt else 0
			idx += 4

if __name__== "__main__":
	main()
