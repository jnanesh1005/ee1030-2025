import ctypes
import numpy as np
import matplotlib.pyplot as plt

LIB_PATH = './planes.so' 
NUM_STEPS = 50
PLOT_RANGE = 10.0


plane_lib = ctypes.CDLL(LIB_PATH)

float_ptr = ctypes.POINTER(ctypes.c_float)

plane_lib.free_points.argtypes = [float_ptr]
plane_lib.free_points.restype = None
plane_lib.generate_plane_1_points.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int]
plane_lib.generate_plane_1_points.restype = float_ptr

plane_lib.generate_plane_2_points.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int]
plane_lib.generate_plane_2_points.restype = float_ptr

plane_lib.generate_plane_3_points.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int]
plane_lib.generate_plane_3_points.restype = float_ptr

plane_lib.generate_plane_4_points.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int]
plane_lib.generate_plane_4_points.restype = float_ptr


def get_plane_data(c_function, *args):
    points_ptr = None
    points_data = None
    total_points = NUM_STEPS * NUM_STEPS
    
    try:
        points_ptr = c_function(*args)
        if not points_ptr:
            raise MemoryError("C function failed to allocate memory or returned NULL.")
        
        points_np_view = np.ctypeslib.as_array(points_ptr, shape=(total_points * 3,))
        
        points_data = np.copy(points_np_view)

    finally:
        if points_ptr:
            plane_lib.free_points(points_ptr)

    return points_data

print("Generating points for all planes...")

plane1_data_flat = get_plane_data(
    plane_lib.generate_plane_1_points, 
    -PLOT_RANGE, PLOT_RANGE, -PLOT_RANGE, PLOT_RANGE, NUM_STEPS
)
plane2_data_flat = get_plane_data(
    plane_lib.generate_plane_2_points,
    -PLOT_RANGE, PLOT_RANGE, -PLOT_RANGE, PLOT_RANGE, NUM_STEPS
)
plane3_data_flat = get_plane_data(
    plane_lib.generate_plane_3_points,
    -PLOT_RANGE, PLOT_RANGE, -PLOT_RANGE, PLOT_RANGE, NUM_STEPS
)
plane4_data_flat = get_plane_data(
    plane_lib.generate_plane_4_points,
    -PLOT_RANGE, PLOT_RANGE, -PLOT_RANGE, PLOT_RANGE, NUM_STEPS
)

print(f"Generated {plane1_data_flat.shape[0] // 3} points per plane and freed C memory.")

def reshape_for_plot(flat_data):
    points = flat_data.reshape(NUM_STEPS * NUM_STEPS, 3)
    X = points[:, 0].reshape(NUM_STEPS, NUM_STEPS)
    Y = points[:, 1].reshape(NUM_STEPS, NUM_STEPS)
    Z = points[:, 2].reshape(NUM_STEPS, NUM_STEPS)
    return X, Y, Z

X1, Y1, Z1 = reshape_for_plot(plane1_data_flat)
X2, Y2, Z2 = reshape_for_plot(plane2_data_flat)
X3, Y3, Z3 = reshape_for_plot(plane3_data_flat)
X4, Y4, Z4 = reshape_for_plot(plane4_data_flat)

print("Plotting the planes...")
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X1, Y1, Z1, cmap='viridis', alpha=0.7)
ax.plot_surface(X2, Y2, Z2, cmap='plasma', alpha=0.7)
ax.plot_surface(X3, Y3, Z3, cmap='inferno', alpha=0.7)
ax.plot_surface(X4, Y4, Z4, cmap='magma', alpha=0.7)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('planes')
plt.savefig("./figs/planes.png")
plt.show()

