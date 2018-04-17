import sys
list=[]
f=open(sys.argv[1],"r") 
for line in f:
	list.append((float)(line))
print list
