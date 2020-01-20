import numpy as np
from mnist import MNIST
import matplotlib.pyplot as plt
from pylab import cm
from common.functions import sigmoid, softmax

INNODES = 784
HNODES = 100
ONODES = 10
PIC_NUM = 10000

# 前処理
def init_network():
    network = {}
    # 中間層の間のWとb
    sh = np.sqrt(1/784)
    np.random.seed(seed=32)
    network['W1'] = np.random.normal(0, sh, (INNODES, HNODES)) # (784, 100)
    network['b1'] = np.random.normal(0, sh, (1, HNODES)) # (1, 100)
    # 出力層の間のWとb
    so = np.sqrt(1/100)
    network['W2'] = np.random.normal(0, so, (HNODES, ONODES)) # (100, 10)
    network['b2'] = np.random.normal(0, so, (1, ONODES)) # (1, 10)
    return network

def forward(network, x):
    W1, W2 = network['W1'], network['W2']
    b1, b2 = network['b1'], network['b2']

    # 中間層へ
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1) # (1, 100)
    # 出力層へ
    a2 = np.dot(z1, W2) + b2 # (1, 10)
    y = softmax(a2)

    return y

mndata = MNIST("/Users/daisuke/le4nn/")
x_test, t_test = mndata.load_testing()
x_test = np.array(x_test)
t_test = np.array(t_test)

print("0~9999までの整数を入力してください")
idx = int(input())
x = x_test[idx]
network = init_network()
y = forward(network, x)
print("一番確率が高いのは", np.argmax(y))