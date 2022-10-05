import numpy as np
import MNIST

def perceptron(x, y, tau):
    N = x.shape[0] # number of training examples
    d = x.shape[1] # dimension of each training example
    
    th = np.zeros((d,1)) # initialize theta to all zeros (th in R^d)
    th_0 = 0
    for t in range(tau): # tau is the number of iterations
        for i in range(N): 
            if(y[i]*(th.T @ x[i]) <= 0): # if the prediction is wrong
                th = th + y[i]*x[i] # update theta
                th_0 = th_0 + y[i] # update theta_0
    return th, th_0
