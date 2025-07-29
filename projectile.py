import matplotlib.pyplot as plt
import math
x=[]
y=[]
ispeed=float(input("launch speed?\n"))
degrees=float(input("angle of launch?\n"))

radians = math.radians(degrees)
if degrees==90:
    xspeed=0
else:
    xspeed=ispeed*math.cos(radians)    

radians = math.radians(degrees)
t=float(0)
yspeed=ispeed*math.sin(radians)


xval=1
yval=1
xindex=0
while yval>=0:
    yval=t*yspeed - 9.81*t*t*0.5
    xval=t*xspeed 
    if yval>=0:
        y.append(yval)
        x.append(xval)
    xindex=xindex+1    
  
    t=t+.001
xindex=xindex//2 

x.append(t * xspeed)
y.append(0)
if y[-1]<0 or y[0]<0:
    y[0]=0

    y[-1]=0    
tops=max(y)+10
plt.plot(x,y,label="object trijectory")
plt.ylim(bottom=0,top=tops)
plt.gca().set_aspect('equal')
plt.xlabel("Distance")
plt.ylabel("Hight")
plt.text(x[xindex], -50, "Zoom in for better visibility at high angles or very low speeds.\n", 
         fontsize=9, bbox=dict(facecolor='yellow', alpha=0.5),
         horizontalalignment='center')
plt.title(f"Launch at {degrees}° with {ispeed} m/s")
peak_index = y.index(max(y))
plt.plot(x[peak_index], y[peak_index], 'ro')
plt.text(x[peak_index], y[peak_index]+1, "Peak", color='red')
plt.grid(True)
plt.legend()
plt.show()
