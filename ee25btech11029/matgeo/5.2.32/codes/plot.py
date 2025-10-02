import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib_path = './line_plotter.so'


line_lib = ctypes.CDLL(lib_path)


line_lib.get_y_for_line1.argtypes = [ctypes.c_double]
line_lib.get_y_for_line1.restype = ctypes.c_double

line_lib.get_y_for_line2.argtypes = [ctypes.c_double]
line_lib.get_y_for_line2.restype = ctypes.c_double

x_values = np.linspace(-10, 10, 100)

y1_values = [line_lib.get_y_for_line1(x) for x in x_values]
y2_values = [line_lib.get_y_for_line2(x) for x in x_values]

plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(10, 8))

plt.plot(x_values, y1_values, label='x + 2y - 4 = 0', color='dodgerblue', linewidth=2)
plt.plot(x_values, y2_values, label='2x + 4y - 12 = 0', color='tomato', linewidth=2, linestyle='--')

plt.title('Plot of Linear Equations', fontsize=16, fontweight='bold')
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)
plt.legend(fontsize=10)

plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('equal')
plt.savefig("./figs/lines.png") 
plt.show()

