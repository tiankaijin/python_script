import sys
print "plt.xlabel('zip_%s')" % sys.argv[1]
if sys.argv[2]=="10p":
	print "plt.ylabel('sta>=4 ratio')"
else:
	print "plt.ylabel('multicast ratio')"
if sys.argv[1]=='r':
	print "x = [0.0,0.2,0.4,0.6,0.8,1.0]"
else:
	print "x = [0.2,0.4,1.0,1.2,2.0]"

for i in range(1,6,1):
	print """plt.plot(x,sta%d,"x-",label="sta%d")""" % (i*4,i*4)
print """plt.grid(True)\n  
legend=plt.legend(bbox_to_anchor=(1.0, 0.45), loc=1, borderaxespad=0.)\n  
frame = legend.get_frame()\n
frame.set_facecolor('none')\n"""
if sys.argv[1]=='r':
	print """plt.title("%s=%s")""" % ("a",sys.argv[3])
else:
	print """plt.title("%s=%s")""" % ("r",sys.argv[3])
print "plt.show()"

