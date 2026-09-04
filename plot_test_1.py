import matplotlib.pyplot as plt

#Createemptyarrays
X=[]
Y=[]

#Open file in read mode
inFile=open("Pmotion_output.txt","r")
for line in inFile:
    t,x,y,v_x,v_y=line.split(" ")
    X.append(float(x))
    Y.append(float(y))
inFile.close()

#Create the x vs y plot
plt.xlabel("$x$(m)")
plt.ylabel("$y$(m)")
plt.plot(X,Y)
plt.show()

#plt.savefig("Pmotion_plot.png") in case you want a copy for later
#also PDF uses vector graphics so it is good (still not as good as EPS) for printing, zooming, resizing etc. did not know that.