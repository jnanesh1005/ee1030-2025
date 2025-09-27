import numpy as np
import matplotlib.pyplot as plt

def plot_plane_from_points():

    x_range = np.linspace(-1, 4, 20)
    y_range = np.linspace(-1, 4, 20)
    X, Y = np.meshgrid(x_range, y_range)

    Z = (3/2) - (1/2) * X + (3 / 4) * Y

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(X, Y, Z, alpha=0.7, cmap='plasma', edgecolor='none')


    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Plane Passing Through Three Points')
    ax.legend()

    ax.set_xlim([-1, 4])
    ax.set_ylim([-1, 4])
    ax.set_zlim([-1, 6])
    plt.savefig("./figs/plane2.png")
    plt.show()

if __name__ == '__main__':
    plot_plane_from_points()

