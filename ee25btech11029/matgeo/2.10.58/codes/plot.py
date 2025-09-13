import ctypes
import numpy as np
import matplotlib.pyplot as plt

parallelogram_lib = ctypes.CDLL("./points.so")

parallelogram_lib.get_points.argtypes = [np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C")]

points = np.zeros(8, dtype=np.double)

parallelogram_lib.get_points(points)


points = points.reshape((4,2))

points = np.vstack([points, points[0]])

plt.plot(points[:,0], points[:,1], "bo-")
plt.title("Paralleogram from C library")
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().set_aspect("equal")
plt.grid(True)
plt.savefig('figs/parallelogram.png')
plt.show()
