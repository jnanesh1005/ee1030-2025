import ctypes
import numpy as np
import matplotlib.pyplot as plt
import subprocess
y=input("are you using termux?(y/n)=")


lib = ctypes.CDLL('./vectors.so')

lib.get_start_points.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.get_end_points.argtypes = [ctypes.POINTER(ctypes.c_double)]

n_lines = 4

start_points = np.zeros((n_lines,3), dtype=np.float64)
end_points   = np.zeros((n_lines,3), dtype=np.float64)
lib.get_start_points(start_points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
lib.get_end_points(end_points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = ['r','g','b','m']
label=['alpha','beta','beta1','beta2']
for i in range(n_lines):
    xs = [start_points[i,0], end_points[i,0]]
    ys = [start_points[i,1], end_points[i,1]]
    zs = [start_points[i,2], end_points[i,2]]
    ax.plot(xs, ys, zs, color=colors[i], label=label[i])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title("3D Lines from C Library")
fig.savefig('../figs/fig2.png')
if (y=='y'):
    subprocess.run(shlex.split('termux-open ../figs/fig.png'))
else:
    subprocess.run(["open",  "../figs/fig.png"])
plt.show()
