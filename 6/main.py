import sys

class Planet:
	o = []
	name = None
	depth = 0
	parent = None
	def __init__(self, name = "invalid", parent = None, oe = None):
		self.name = name
		self.o = []
		self.parent= parent
		if oe != None:
			self.o.append(oe)
		self.depth = 0

	def incDepth(self, x):
		self.depth += x
		for p in self.o:
			p.incDepth(x)

	def depthSearch(self, d, sender):
		if self.name == "SAN":
			return d
		if len(self.o) == 0 and self.parent == None:
			return -1

		if self.parent != None and self.parent.name != sender:
			retP = self.parent.depthSearch(d+1, self.name)
			if retP > -1:
				return retP

		for op in self.o:
			if op.name == sender:
				continue
			ret = op.depthSearch(d+1, self.name)
			if ret > -1:
				return ret
		return -1

	def findSAN(self):
		return self.depthSearch(0, self.name) - 2 


	def __str__(self):
		return self.name + "(" + str(self.depth) + "):["+ str(self.parent) +"]"

def main():
	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()


	#build planets and direct orbits constilation	
	planets=[]
	for line in lines:
		line = line[0:len(line)-1]
		pls = line.split(")", -1)
		if len(pls) < 2:
			break
		p = pls[0]
		o = pls[1]
		pl = []
		ol = []
		
		#see if mentioned planets are alrdy registered	
		curP = next((x for x in planets if x.name == p), None)
		op = next((x for x in planets if x.name == o), None)		

		#if orbiting one isnt seen yet create it and add it to list
		
		if curP == None:
			curP = Planet(p)
			planets.append(curP)
	
		if op == None:
			op = Planet(o, curP)
			planets.append(op)
			op.depth += 1

		curP.o.append(op)
	
		op.depth += curP.depth
		if op.parent == None:
			op.parent = curP
			op.depth += 1
			for tempp in op.o:
				tempp.incDepth(op.depth)
	

	orbits = 0
	for p in planets:
		#print(p)
		orbits += p.depth
	print(str(orbits))

	#find SAN
	YOU = next((x for x in planets if x.name == "YOU"), None)
	if YOU == None:
		print("YOU not present")
		return
	print(str(YOU.findSAN()))	

if __name__== "__main__":
	main()
