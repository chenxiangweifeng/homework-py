import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 10)
y1, y2 = np.sin(x), np.cos(x)

plt.plot(x, y1, 'ro-')
plt.plot(x, y2, 'g*:', ms=10)
plt.show()