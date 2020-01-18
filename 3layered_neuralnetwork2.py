import numpy as np
from mnist import MNIST
import matplotlib.pyplot as plt
from pylab import cm
from common.functions import *

INNODES = 784
HNODES = 100
ONODES = 10
PIC_NUM = 10000
BATCH = 100

# 前処理
def init_network():
    network = {}
    # 中間層の間のWとb
    sh = np.sqrt(1/784)
    np.random.seed(seed=32)
    network['Wh'] = np.random.normal(0, sh, (HNODES, INNODES))
    network['bh'] = np.random.normal(0, sh, (HNODES, 1))
    # 出力層の間のWとb
    so = np.sqrt(1/100)
    network['Wo'] = np.random.normal(0, so, (ONODES, HNODES))
    network['bo'] = np.random.normal(0, so, (ONODES, 1))
    return network

# 入力層での入力->出力
def innodes_cal(x):
    return x

# 中間層での入力->出力
def hnodes_cal(yin, network):
    ah = np.dot(yin, network['Wh'].T) + network['bh'].T
    yh = sigmoid(ah)
    return yh

# 後処理、出力層での入力->出力
def onodes_cal(yh, network):
    ao = np.dot(yh, network['Wo'].T) + network['bo'].T
    yo = softmax(ao)
    return yo

# エントロピー誤差
def cross_entropy(y, t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))

# ミニバッチ
def mini_batch(e) :
    En = np.sum(e)/BATCH
    return En

mndata = MNIST("/Users/daisuke/le4nn/")
X, Y = mndata.load_training()
X = np.array(X)
Y = np.array(Y)
ran_num = np.random.choice(X.shape[0], BATCH)
x = X[ran_num, :]
y = Y[ran_num]
network = init_network()

yin = innodes_cal(x)
yh = hnodes_cal(yin, network)
yo = onodes_cal(yh, network)
t = np.eye(10)[y]

print("結果")
print(mini_batch(cross_entropy(yo, t)))