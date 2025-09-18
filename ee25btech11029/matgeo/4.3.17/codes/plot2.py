import numpy as np
import matplotlib.pyplot as plt

def plot_plane_from_points():
    p1 = np.array([2, 0, 0])
    p2 = np.array([0, 3, 0])
    p3 = np.array([0, 0, 4])

    x_range = np.linspace(-1, 4, 20)
    y_range = np.linspace(-1, 4, 20)
    X, Y = np.meshgrid(x_range, y_range)

    Z = 4 - 2 * X - (4 / 3) * Y

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(X, Y, Z, alpha=0.7, cmap='plasma', edgecolor='none')

    ax.scatter(p1[0], p1[1], p1[2], color='red', s=120, label='(2,0,0)', depthshade=False)
    ax.scatter(p2[0], p2[1], p2[2], color='red', s=120, label='(0,3,0)', depthshade=False)
    ax.scatter(p3[0], p3[1], p3[2], color='red', s=120, label='(0,0,4)', depthshade=False)
    ax.text(2.1,0.1,0.1,"A",color="black")
    ax.text(0.1,3.1,0.1,"B",color="black")
    ax.text(0.1,0.1,4.1,"C",color="black")


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
