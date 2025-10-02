import numpy as np
import matplotlib.pyplot as plt

def get_y_for_line1(x):
    # Equation 1: x + 2y - 4 = 0  =>  y = (4 - x) / 2
    return (4 - x) / 2

def get_y_for_line2(x):
    # Equation 2: 2x + 4y - 12 = 0 =>  y = (12 - 2x) / 4
    return (12 - 2 * x) / 4

x_values = np.linspace(-10, 10, 100)

y1_values = get_y_for_line1(x_values)
y2_values = get_y_for_line2(x_values)

plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(10, 8))

plt.plot(x_values, y1_values, label='x + 2y - 4 = 0', color='dodgerblue', linewidth=2)
plt.plot(x_values, y2_values, label='2x + 4y - 12 = 0', color='tomato', linewidth=2, linestyle='--')

plt.title('Plot of Linear Equations', fontsize=16, fontweight='bold')
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)
plt.legend(fontsize=10)
plt.savefig("./figs/lines2.png") 
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('equal')

plt.show()
