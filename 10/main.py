import sys
import functools

def cmpf(x,y):
	d1 = abs(26 - x[0]) + abs(36 - x[1])
	d2 = abs(26 - y[0]) + abs(36 - y[1])
	return d1 - d2

def main():
	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()
	
	field = []
	ast = []
	yline = 0
	for line in lines:
		if(len(line) <2):
			break
		for x in range(len(line)):
			if(line[x] == '#'):
				ast.append((x,yline))
		field.append(line[0:len(line)-1])
		yline +=1

	#print(field)

	w=len(field[0])
	h=len(field)

	#print(w,h)
	#print(ast)

	best = 0
	
	i = ast [8]
	for i in ast:
		angles = []
		s = 0
		for j in ast:
			dx = j[0] - i[0]
			dy = j[1] - i[1]
			q = 1 if dx > 0 and dy >= 0 else 2 if dx >= 0 and dy < 0 else 3 if dx < 0 and dy <= 0 else 4 if dx <= 0 and dy > 0 else 0
			if dx != 0:
				v = dy/float(dx)
			else:
				v = 1000000 if dy > 0 else -1000000
			if (q, v) not in angles:
				angles.append((q, v))
				s +=1
		if s > best:
			best = s
			bestA = i

	print(best-1)
	print(bestA)



	lep = []
	for x in range(bestA[0], w):
		lep.append((x, 0))
	for y in range(0, h):
		lep.append((w-1, y))	
	for x in range(w-1, 0):
		lep.append((x, h-1))
	for y in range(h-1, 0):
		lep.append((0, y))
	for x in range(0, bestA[0]):
		lep.append((x,0))

	i = bestA
	lastA = None
	by = bestA[1]
	field[by] = field[by][0:bestA[0]] + "B" + field[by][bestA[0]+1:w]

	#sorted(ast, key=lambda x : (abs(i[0] - x[0]) + abs(i[1] - x[1])))

	for s in range(len(ast)):
		for t in range(len(ast)):
			if cmpf(ast[s], ast[t]) < 0:
				temp = ast[s]
				ast[s] = ast[t]
				ast[t] = temp


	if i != None:
		hc = 0
		while hc < 200:
			for l in lep:
				if hc >= 200:
					break
				angles = []
				for j in ast:
					dx = j[0] - i[0]
					dy = j[1] - i[1]

					dxl = l[0] - i[0]
					dyl = l[1] - i[1]
					q = 1 if dx > 0 and dy >= 0 else 2 if dx >= 0 and dy < 0 else 3 if dx < 0 and dy <= 0 else 4 if dx <= 0 and dy > 0 else 0
					ql = 1 if dxl > 0 and dyl >= 0 else 2 if dxl >= 0 and dyl < 0 else 3 if dxl < 0 and dyl <= 0 else 4 if dxl <= 0 and dyl > 0 else 0
					if dx != 0:
						v = dy/float(dx)
					else:
						v = 1000000 if dy > 0 else -1000000
					if dxl != 0:
						vl = dyl/float(dxl)
					else:
						vl = 1000000 if dyl > 0 else -1000000
		
					if v == vl and q == ql:
						hc +=1
						field[j[1]] = field[j[1]][0:j[0]] + "X" + field[j[1]][j[0]+1:w]
						if hc == 200:
							field[j[1]] = field[j[1]][0:j[0]] + "@" + field[j[1]][j[0]+1:w]
						lastA = j
						break
	
	for row in field:
		print(''.join(row))



	print(lastA[0]*100+lastA[1])
	print(lastA)
if __name__== "__main__":
	main()
