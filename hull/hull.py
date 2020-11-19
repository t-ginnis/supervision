import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import pandas as pd
import numpy as np

labels= ['Num A','Num B','Energy']
d=np.array([
   [1,0,2,1,1],
   [0,1,1,1,2],
   [-112.2,-345.1,-571.1,-462.7,-808.5]
   ])
d=np.transpose(d)



df=pd.DataFrame(data=d,columns=labels)

df["Tot"]=df["Num A"]+df["Num B"]
df['x']=df["Num A"]/df["Tot"]
AE=df['Energy'][0]
BE=df['Energy'][1]
df['rel_E']=(df['Energy']-AE*df['Num A']-BE*df['Num B'])/df["Tot"]
points=np.array([[df['x'][i],df['rel_E'][i]] for i in range(len(df['x']))])
#print(points)
hull=ConvexHull(points)

plt.plot(points[:,0],points[:,1],'ro')
c=0
for simplex in hull.simplices:
    if c!=0:
        plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
    c+=1


plt.xlabel('x in A$_x$B$_{1-x}$')
plt.ylabel('Formation Energy per atom / eV ')
plt.title('Convex Hull for AB binary system')

plt.savefig('hull.png',dpi=600)
