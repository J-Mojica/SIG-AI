import numpy as np
import MNIST

def perceptron(x, y, tau):
    th = np.zeros((x.shape[1],1))
    th_0 = 0
    for t in range(tau):
        for i in range(x.shape[0]):
            if(y[i]*(th.T @ x[i]) <= 0):
                th = th + y[i]*x[i]
                th_0 = th_0 + y[i]
    return th, th_0
