# 03-5 MNIST
## import
import numpy as np
import os.path
import pickle
import time
from dataset.mnist import load_mnist    #dataset 하위 디렉토리에 mnist.py 파일에서 load_mnist 함수 import

## 함수 정의
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(a):
    max = np.max(a)             # 오버플로 대책 (93.p)
    exp_a = np.exp(a - max)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y
    
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    
    return x_test, t_test

def init_network():
    file_path = os.path.dirname(os.path.abspath(__file__))  + "\dataset\sample_weight.pkl"
    with open(file_path, 'rb') as f:
        network = pickle.load(f)
    
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    
    return y

## 처리 시작
tt = time.time()
print(tt)
print(time.strftime('%X %S', time.localtime(tt)))
x, t = get_data()
network = init_network()

batch_size = 1000
accuracy_cnt = 0
for i in range(0, len(x), batch_size):
    y = predict(network, x[i:i+batch_size])
    p = np.argmax(y, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])
        
print("Accuracy:"+str(float(accuracy_cnt)/len(x)))
tt = time.time()
print(tt)
print(time.strftime('%X %S', time.localtime(tt)))