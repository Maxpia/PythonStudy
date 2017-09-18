# 04-2 MNIST_minibatch
## import
import numpy as np
import matplotlib.pylab as plt
#from dataset.mnist import load_mnist    #dataset 하위 디렉토리에 mnist.py 파일에서 load_mnist 함수 import

## 함수 정의
def numerical_diff(f, x):
    h = 1e-4    #1e-50과 같이 너무 자게 하면 반올림 오차로 0.0이 된다. np.float32(1e-50) #0.0
    return (f(x + h) - f(x - h)) / (2 * h)

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x) # x와 형상이 같은 배열을 생성
    
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)
        
        x[idx] = tmp_val - h
        fxh2 = f(x)
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val
        
    return grad

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    
    return x

def function_1(x):
    return 0.01*x**2 + 0.1*x**2

def function_2(x):
    return np.sum(x**2)
    #return x[0]**2 + x[1]**2 #위와 같음
   
def tangent_line(f, x):
    d = numerical_diff(f, x)
    y = f(x) - d*x
    return lambda t: d*t + y
    
## 처리 시작
x = np.arange(0.0, 20.0, 0.1)
'''
y = function_1(x)
tl1 = tangent_line(function_1, 5)
tl2 = tangent_line(function_1, 10)
y1 = tl1(x)
y2 = tl2(x)

plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y, label='f(x)')
plt.plot(x, y1, linestyle='--', label='tl 5')
plt.plot(x, y2, linestyle='-.', label='tl 10')
plt.show()
'''

'''
def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

def function_tmp2(x1):
    return 3.0**2.0 + x1*x1
    
print(numerical_diff(function_tmp1, 3.0), numerical_diff(function_tmp2, 4.0))
print(numerical_diff(function_tmp1, 0.0), numerical_diff(function_tmp2, 2.0))
print(numerical_diff(function_tmp1, 3.0), numerical_diff(function_tmp2, 0.0))

print(numerical_gradient(function_2, np.array([3.0, 4.0])))
print(numerical_gradient(function_2, np.array([0.0, 2.0])))
print(numerical_gradient(function_2, np.array([3.0, 0.0])))
'''

init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x, lr=0.1, step_num=100))