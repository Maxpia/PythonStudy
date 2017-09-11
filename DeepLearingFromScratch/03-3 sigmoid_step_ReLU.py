# sigmoid.py
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def step_function(x):
    return np.array(x > 0, dtype=np.int)
    
def ReLU(x):
    return np.maximum(0, x)
    
x = np.arange(-5., 5., .1)
y1 = sigmoid(x)
y2 = step_function(x)
y3 = ReLU(x)
plt.plot(x, y1, label='sigmoid')
plt.plot(x, y2, linestyle='--', label='step')
plt.plot(x, y3, linestyle='-.', label='ReLU')
plt.title('sigmoid & step & ReLU')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-5.1, 5.1)
plt.ylim(-0.1, 5.1)
plt.legend()
plt.show()
