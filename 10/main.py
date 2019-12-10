import sys
import functools
import math

xb=26
yb=36

def cmpf(x,y):
	d1 = abs(xb - x[0]) + abs(yb - x[1])
	d2 = abs(xb - y[0]) + abs(yb - y[1])
	return d1 - d2

def printField(f):
	for row in f:
		print(''.join(row))

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

	w=len(field[0])
	h=len(field)

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

	xb=bestA[0]
	yb=bestA[1]


	acc=10
	r = int(math.log10(acc))
	step=1/acc
	lep=[]
	cura=0

	#fill lep with all possible angles with given accuracy	
	while math.floor(cura) < 360:
		lep.append(cura)
		cura = round(cura + step,1)	

	k = 270*acc

	i = bestA
	ast.remove(bestA)
	lastA = None
	by = bestA[1]
	field[by] = field[by][0:bestA[0]] + "B" + field[by][bestA[0]+1:w]


	#sort doenst work
	sorted(ast, key=lambda x : (abs(i[0] - x[0]) + abs(i[1] - x[1])))

	#just braindead sort it
	for s in range(len(ast)):
		for t in range(len(ast)):
			dxs = bestA[0] - ast[s][0]
			dys = bestA[1] - ast[s][1]
			tas = round((math.atan2(dys,dxs)*360/2/math.pi-90)%360,r)
			dxt = bestA[0] - ast[t][0]
			dyt = bestA[1] - ast[t][1]
			tat = round((math.atan2(dyt,dxt)*360/2/math.pi-90)%360,r)
			if tas< tat: 
				temp = ast[s]
				ast[s] = ast[t]
				ast[t] = temp
			if tas == tat and cmpf(ast[s], ast[t]) > 0:
				temp = ast[s]
				ast[s] = ast[t]
				ast[t] = temp

	if i != None:
		hc = 0
		while hc < 200:
			first = 0
			while True:
				l = lep[k]
				if hc >= 200:
					break
				angles = []
				for j in ast:
					dx = i[0] - j[0]
					dy = i[1] - j[1]
					
					ta = round((math.atan2(dy,dx)*360/2/math.pi-180)%360, r)
					if ta == l:
						ast.remove(j)
						hc +=1
						field[j[1]] = field[j[1]][0:j[0]] + str(hc%10) + field[j[1]][j[0]+1:w]
						if hc == 200:
							field[j[1]] = field[j[1]][0:j[0]] + "@" + field[j[1]][j[0]+1:w]
						lastA = j
						break
				if k == len(lep)-1:
					k = 0
				else:
					k+=1
	
	print(lastA[0]*100+lastA[1])
	print(lastA)
if __name__== "__main__":
	main()
