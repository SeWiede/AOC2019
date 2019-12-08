import sys
import itertools
import subprocess


def getAMP(setting, AMP):
	prog = subprocess.Popen(["python", "../5/main.py", sys.argv[1]],
							stdin=subprocess.PIPE,
							stdout=subprocess.PIPE)
	prog.stdin.write(str(setting)+"\n")
	prog.stdin.write(str(AMP) + "\n")

	
	ret = -1
	x = ""
	try:
		x = prog.stdout.readline()
		ret = int(x)
	except:
		print(x)

	return ret


def main():
	
	perms = list(itertools.permutations([0,1,2,3,4]))
	test = [0,1,2,3,4]	

	maxthrust = 0
	maxperm= []
	for cl in perms:
		AAmp = getAMP(cl[0], 0)
		BAmp = getAMP(cl[1], AAmp)
		CAmp = getAMP(cl[2], BAmp)
		DAmp = getAMP(cl[3], CAmp)
		EAmp = getAMP(cl[4], DAmp)
		if EAmp > maxthrust:
			maxthrust = EAmp
			maxperm = cl
		

	print(maxthrust)
	print(cl)

if __name__== "__main__":
	main()
