import numpy as np
import matplotlib.pyplot as plt

points=np.array([[-2,-1],[4,0],[3,3],[-3,2]])
points=np.vstack([points,points[0]])
plt.plot(points[:,0],points[:,1],"bo-",linewidth=2)
plt.title("Parallelogram of 4 Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect("equal")
plt.grid(True)
plt.savefig('figs/parallelogram2.png')
plt.show()


