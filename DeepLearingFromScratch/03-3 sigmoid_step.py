# sigmoid.py
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def step_function(x):
    return np.array(x > 0, dtype=np.int)
    
x = np.arange(-5., 5., .1)
y1 = sigmoid(x)
y2 = step_function(x)
plt.plot(x, y1, label='sigmoid')
plt.plot(x, y2, linestyle='--', label='step')
plt.title('sigmoid & step')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-0.1, 1.1)
plt.legend()
plt.show()
