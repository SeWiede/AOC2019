import sys
import math

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



	offset = 1000
	codes = [0]*offset + codes + [0]*offset
	idx = offset
	rb = 0	
	while True:
		op =codes[idx]%100 #is 0x anyway
		if op == 99:
			break
		C = math.floor(codes[idx]/100%10)
		B = math.floor(codes[idx]/1000%10)
		A = math.floor(codes[idx]/10000%10)
		idx1 = codes[idx+1]+offset
		idx2 = codes[idx+2]+offset
		idx3 = codes[idx+3]+offset
	
		if op == 3:
			i = sys.stdin.readline()
			try:
				n = int(i)
				if C == 2:
					codes[rb+idx1] =n
				if C == 1:
					 codes[idx+1]
				if C== 0:
					codes[idx1] = n
			except:
				print("no digit given", file=sys.stderr)
				return
			idx += 2
			continue
		if op == 4:
			if C == 2:
				print(codes[rb+idx1])
			if C == 1:
				print(codes[idx+1])
			if C == 0:
				print(codes[idx1])
			idx += 2
			continue
		if op == 9:
			if C==0:
				rb += codes[idx1]
			if C==1:
				rb += idx1-offset
			if C==2:
			 	rb += codes[rb+idx1]
			idx += 2
			continue

		rd = codes[idx1] if C==0 else idx1-offset if C==1 else codes[rb+idx1]
		rt = codes[idx2] if B==0 else idx2-offset if B==1 else codes[rb+idx2]
		
		g = idx3 if A==0 else idx+3 if A==1 else rb+idx3 

		if op == 1:	
			rs = rd + rt
			codes[g] = rs
			idx += 4
			continue
		if op == 2:
			rs = rd * rt
			codes[g] = rs
			idx += 4
			continue
		if op == 5:
			idx = rt+offset if rd else idx+3
			continue
		if op == 6:
			idx = rt+offset if not rd else idx+3
			continue
		if op == 7:			
			codes[g] = 1 if rd < rt else 0
			idx += 4
			continue
		if op == 8:			
			codes[g] = 1 if rd == rt else 0
			idx += 4
			continue

		print("WRONG OPCODE: " + str(op) + " at index: " + str(idx-offset), file=sys.stderr)
		break

if __name__== "__main__":
	main()
