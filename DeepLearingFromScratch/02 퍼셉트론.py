# 퍼셉트론.py
import numpy as np

def AND(x1, x2):
    W1, W2, theta = 0.5, 0.5, 0.7
    tmp = x1*W1 + x2* W2
    if tmp <= theta:
        return ("%d AND %d : 0" % (x1, x2))
    else:
        return ("%d AND %d : 1" % (x1, x2))
        
print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))

print("")

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([.5, .5])
    b = -.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return ("%d AND %d : 0" % (x1, x2))
    else:
        return ("%d AND %d : 1" % (x1, x2))
        
print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))

print("")

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-.5, -.5])
    b = .7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return ("%d NAND %d : 0" % (x1, x2))
    else:
        return ("%d NAND %d : 1" % (x1, x2))
        
print(NAND(0, 0))
print(NAND(1, 0))
print(NAND(0, 1))
print(NAND(1, 1))

print("")

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([.5, .5])
    b = -.2
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return ("%d OR %d : 0" % (x1, x2))
    else:
        return ("%d OR  %d : 1" % (x1, x2))
        
print(OR(0, 0))
print(OR(1, 0))
print(OR(0, 1))
print(OR(1, 1))

print("")

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([.5, .5])
    b = -.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1
        
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-.5, -.5])
    b = .7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1
        
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([.5, .5])
    b = -.2
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1
        
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return ("%d XOR %d : %d" % (x1, x2, y))
        
print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))

