import sys
import itertools
import subprocess
import math

class Rec:
	ing = []
	result = None

	def __init__(self, inga, res):
		temp = []
		for i in inga:
			l = i.split(' ')
			le = (int(l[0]), l[1])
			temp.append(le)
		self.ing = temp
		temp = res.split(' ')
		self.result = (int(temp[0]), temp[1])

	def __str__(self):
		return str(self.ing) + " => " + str(self.result[0]) + " " + self.result[1]

#this works for exact relations
def countOres(ings, rs, n =1):
	ores = 0
	for ing in ings:
		#print(n, ing)
		if "ORE" in ing[1]:
			#print("add " + str(ing[0]*n) + " ores")
			ores += ing[0]*n
		for rec in rs:
			if ing[1] ==  rec.result[1]:
				ores += n*countOres(rec.ing, rs, ing[0]/rec.result[0])	
	return ores

	
def updateMadeList(recs, made, res):
	isin=False
	for m in made:
		if m[1] == res[1]:
			if  m[1] == "ORE":
				made.remove(m)
				made.append((m[0] + res[0], m[1]))
				return
		
			leftover = m[0] - m[2]	
			isin=True
			rece = [x for x in recs if x.result[1] == m[1]][0]
			ho = math.ceil((res[0]-leftover)/rece.result[0])
			
			made.remove(m)
			made.append((m[0] + ho*rece.result[0], m[1], m[2]+res[0]))
			for i in rece.ing:
				updateMadeList(recs,made, (i[0]*ho, i[1]))	
			break
	if not isin:
		if res[1] == "ORE":
			made.append(res)
			return
		rece = [x for x in recs if x.result[1] == res[1]][0]
		ho = math.ceil(res[0]/rece.result[0])
		made.append((rece.result[0] * ho, res[1], res[0]))
		for i in rece.ing:
			updateMadeList(recs,made, (i[0]*ho, i[1]))
			


def main():
	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()
	
	receipes=[]
	fr = None
	for line in lines:
		if len(line) < 5:
			break
		line = line.replace('\n', '')
		r= line.split(" => ")
		nr = Rec(r[0].split(", "), r[1])
		if "FUEL" in r[1]:
			fr =nr
		receipes.append(nr)	

	needed = fr.ing
	m = 1
	ores = countOres(needed, receipes, m)/m


	made = []
	updateMadeList(receipes, made, fr.result)
	ores = 0
	for m in made:
		if m[1] == "ORE":
			ores+=m[0]

	print(ores)

	maxores=1000000000000
	made = []
	start = math.floor(maxores/ores) #lowerbound
	lasti = start
	step = 100000000
	#I call it binary search :)	
	while step > 0:
		while True:
			made=[]
			updateMadeList(receipes, made, (lasti, "FUEL"))
			ores = 0
			for m in made:
				if m[1] == "ORE":
					ores+=m[0]
			if ores > maxores:
				break
			lasti += step
		print("intermediate " + str(step))
		print(lasti, ores)
		lasti -=step
		step //= 10
	print(lasti)

if __name__== "__main__":
	main()
