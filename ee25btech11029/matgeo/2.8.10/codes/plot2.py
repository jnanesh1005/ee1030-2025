import numpy as np
import matplotlib.pyplot as plt
import sys
import subprocess
print('Using termux?(y/n)')
y = input()
 




alpha=np.array([3,-1,0])
beta=np.array([2,1,-3])
beta1=np.array([3/2,-1/2,0])
beta2=np.array([1/2,3/2,-3])
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot([0,alpha[0]],[0,alpha[1]],[0,alpha[2]],'b-',label='alpha')
ax.plot([0,beta[0]],[0,beta[1]],[0,beta[2]],'g-',label='beta')
ax.plot([0,beta1[0]],[0,beta1[1]],[0,beta1[2]],'r-',label='beta1')
ax.plot([0,beta2[0]],[0,beta2[1]],[0,beta2[2]],color='pink',label='beta')
 

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend(loc='best')
ax.grid(True)
ax.axis('equal')
fig.savefig('../figs/fig.png')
print('Saved figure to ../figs/fig.png')

if(y == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig.png'))
else:
    subprocess.run(["open",  "../figs/fig.png"])
 
plt.show()
