# 04-1 MNIST_study
#import
import numpy as np

#평균 제곱 오차 함수
# E = ½∑(ｙ-ｔ)² : y는 신경망 출력, t는 정답 레이블
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

#평균 제곱 오차 테스트
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

print('mean_squared_error')
y = [.1, .05, .6, .0, .05, .05, .0, .1, .0, .0]

print(mean_squared_error(np.array(y), np.array(t)))

y = [.1, .05, .1, .0, .05, .05, .0, .6, .0, .0]

print(mean_squared_error(np.array(y), np.array(t)))

#교차 엔트로피 오차 함수
# E = -∑ｔlogｙ
def cross_entropy_error(y, t):
    delta = 1e-7    # y가 0이면 마니너스 무한대가 되기때문에 매우 작은 값을 더해 준다.
    return -np.sum(t * np.log(y + delta))
    
print('cross_entropy_error')
y = [.1, .05, .6, .0, .05, .05, .0, .1, .0, .0]

print(cross_entropy_error(np.array(y), np.array(t)))

y = [.1, .05, .1, .0, .05, .05, .0, .6, .0, .0]

print(cross_entropy_error(np.array(y), np.array(t)))