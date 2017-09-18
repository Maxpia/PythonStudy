# 04-2 MNIST_minibatch
## import
import numpy as np
from dataset.mnist import load_mnist    #dataset 하위 디렉토리에 mnist.py 파일에서 load_mnist 함수 import

## 함수 정의
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    
    delta = 1e-7    # y가 0이면 마니너스 무한대가 되기때문에 매우 작은 값을 더해 준다.
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t.astype('int')] + delta)) / batch_size

## 처리 시작
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]
batch_size = 10
batch_mark = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mark]
t_batch = t_train[batch_mark]

print(batch_mark)
print(x_batch.shape)
print(t_batch.shape)

print(cross_entropy_error(np.array(x_batch), np.array(t_batch)))