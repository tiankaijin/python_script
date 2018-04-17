import sys
f=open(sys.argv[1],"r") 
if sys.argv[2]=="10p":
	for line in f:
		if line.startswith("sta"):
			print line.split()[-1],
else:
	for line in f:
		if line.startswith("multicast ratio"):
			print line.split()[-1],
f.close()









