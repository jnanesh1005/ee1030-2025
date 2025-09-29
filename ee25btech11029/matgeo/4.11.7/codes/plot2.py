import numpy as np
import matplotlib.pyplot as plt

NUM_STEPS = 50
PLOT_RANGE = 10.0

def generate_plane_1_points_py(y_min, y_max, z_min, z_max, num_steps):
    y = np.linspace(y_min, y_max, num_steps)
    z = np.linspace(z_min, z_max, num_steps)
    Y, Z = np.meshgrid(y, z)
    X = -2.0 * Y - 4.0
    return X, Y, Z

def generate_plane_2_points_py(x_min, x_max, y_min, y_max, num_steps):
    x = np.linspace(x_min, x_max, num_steps)
    y = np.linspace(y_min, y_max, num_steps)
    X, Y = np.meshgrid(x, y)
    Z = (-3.0 * X + Y) / 4.0
    return X, Y, Z

def generate_plane_3_points_py(x_min, x_max, y_min, y_max, num_steps):
    sqrt287 = np.sqrt(287.0)
    A = 23.0 + 3.0 * sqrt287
    B = 53.0 - sqrt287
    C = 4.0 * sqrt287 - 4.0
    D = 104.0
    
    x = np.linspace(x_min, x_max, num_steps)
    y = np.linspace(y_min, y_max, num_steps)
    X, Y = np.meshgrid(x, y)
    Z = (-A * X - B * Y - D) / C
    return X, Y, Z

def generate_plane_4_points_py(x_min, x_max, y_min, y_max, num_steps):
    sqrt287 = np.sqrt(287.0)
    A = 23.0 - 3.0 * sqrt287
    B = 53.0 + sqrt287
    C = -4.0 - 4.0 * sqrt287
    D = 104.0

    x = np.linspace(x_min, x_max, num_steps)
    y = np.linspace(y_min, y_max, num_steps)
    X, Y = np.meshgrid(x, y)
    Z = (-A * X - B * Y - D) / C
    return X, Y, Z

print("Generating points for all planes using Python...")

X1, Y1, Z1 = generate_plane_1_points_py(-PLOT_RANGE, PLOT_RANGE, -PLOT_RANGE, PLOT_RANGE, NUM_STEPS)
X2, Y2, Z2 = generate_plane_2_points_py(-PLOT_RANGE, PLOT_RANGE, -PLOT_RANGE, PLOT_RANGE, NUM_STEPS)
X3, Y3, Z3 = generate_plane_3_points_py(-PLOT_RANGE, PLOT_RANGE, -PLOT_RANGE, PLOT_RANGE, NUM_STEPS)
X4, Y4, Z4 = generate_plane_4_points_py(-PLOT_RANGE, PLOT_RANGE, -PLOT_RANGE, PLOT_RANGE, NUM_STEPS)

print(f"Generated points for {NUM_STEPS*NUM_STEPS} grid locations per plane.")

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
ax.set_title('Planes')
plt.savefig("./figs/planes2.png")
plt.show()

