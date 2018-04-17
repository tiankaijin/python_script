import matplotlib.pyplot as plt  
sta4 = [0.149100257069,0.210526315789,0.313868613139,0.440506329114,0.510582010582]
sta8 = [0.346564885496,0.444444444444,0.505747126437,0.576576576577,0.605691056911]  
sta16 = [0.599471830986,0.607076350093,0.641434262948,0.678527607362,0.664879356568]   
sta24 = [0.752014879107,0.69545154911,0.718628215121,0.696768060837,0.702546296296]
sta28 = [0.764386536374,0.745155607751,0.759530791789,0.718505647263,0.714439655172]
sta32 = [0.766079085279,0.775627615063,0.773059057731,0.761865112406,0.736372646184]
sta40 = [0.862598770852,0.865356265356,0.824925816024,0.773967809657,0.771992818671]
fig,ax = plt.subplots()  
  
plt.xlabel('zip_s')  
plt.ylabel('multicast ratio')  
  
"""set interval for y label"""  
#yticks = range(10,110,10)  
#ax.set_yticks(yticks)  
  
 
"""set min and max value for axes"""  
#ax.set_ylim([10,110])  
#ax.set_xlim([58,42])  
  
x = [0.4,0.8,1.2,1.6,2.0]  
plt.plot(x,sta4,"x-",label="sta4") 
plt.plot(x,sta8,"x-",label="sta8")  
plt.plot(x,sta16,"+-",label="sta12")  
plt.plot(x,sta24,"+-",label="sta24") 
plt.plot(x,sta28,"x-",label="sta28") 
plt.plot(x,sta32,"+-",label="sta32") 
plt.plot(x,sta40,"+-",label="sta40") 
 
"""open the grid"""  
plt.grid(True)  
legend=plt.legend(bbox_to_anchor=(1.0, 0.45), loc=1, borderaxespad=0.)  
frame = legend.get_frame()
frame.set_facecolor('none')
plt.show()
