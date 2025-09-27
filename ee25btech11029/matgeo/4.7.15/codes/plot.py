import ctypes
import numpy as np
import matplotlib.pyplot as plt


lib = ctypes.CDLL("./plane.so")

lib.generate_plane_points.argtypes = [
    ctypes.c_float, ctypes.c_float,
    ctypes.c_float, ctypes.c_float,
    ctypes.c_int
]
lib.generate_plane_points.restype = ctypes.POINTER(ctypes.c_float)

lib.free_points.argtypes = [ctypes.POINTER(ctypes.c_float)]
lib.free_points.restype = None


NUM_STEPS = 50  
total_points = NUM_STEPS * NUM_STEPS
points_ptr = None

try: 
    points_ptr = lib.generate_plane_points(-1.0, 3.0,-1.0, 4.0,NUM_STEPS)

    if not points_ptr:
        raise MemoryError("C function failed to allocate memory.")

   
    points_np = np.ctypeslib.as_array(points_ptr, shape=(total_points, 3))
    points_data = np.copy(points_np)

finally:
   
    if points_ptr:
        lib.free_points(points_ptr)
        print(f"Generated {points_data.shape[0]} points and freed C memory.")


X = points_data[:, 0].reshape(NUM_STEPS, NUM_STEPS)
Y = points_data[:, 1].reshape(NUM_STEPS, NUM_STEPS)
Z = points_data[:, 2].reshape(NUM_STEPS, NUM_STEPS)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')


ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Plane')
ax.legend()
plt.savefig("./figs/plane.png")
plt.show()

