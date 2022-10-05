from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np



def load_zeros_and_ones():
    '''Only loads the zeros and ones from MNIST dataset, changes the labels of zeros to -1,
    and turns the images into column vectors'''
    # load the MNIST dataset
    (train_x, train_y), (test_x, test_y) = mnist.load_data() 

    # only keep the zeros and ones
    new_train_x = train_x[(train_y == 0) | (train_y == 1)]
    new_train_y = train_y[(train_y == 0) | (train_y == 1)]
    new_test_x = test_x[(test_y == 0) | (test_y == 1)]
    new_test_y = test_y[(test_y == 0) | (test_y == 1)]

    # change the labels of zeros to -1
    for i in range(len(new_train_y)):
        if(new_train_y[i] == 0):
            new_train_y[i] = -1
    for i in range(len(new_test_y)):
        if (new_test_y[i] == 0):
            new_test_y[i] = -1

    # turn the images (matrices) into column vectors
    new_train_x_vectors = np.zeros((new_train_x.shape[0], new_train_x.shape[1]*new_train_x.shape[2], 1))
    new_test_x_vectors = np.zeros((new_train_x.shape[0], new_train_x.shape[1]*new_train_x.shape[2], 1))
    for i in range(new_train_x.shape[0]):
        new_train_x_vectors[i] = matrix_to_vector(new_train_x[i])
    for i in range(new_test_x.shape[0]):
        new_test_x_vectors[i] = matrix_to_vector(new_test_x[i])

    return (new_train_x_vectors, new_train_y), (new_test_x_vectors, new_test_y)

def matrix_to_vector(x):
    '''Convert a matrix to a vector'''
    return x.reshape(x.shape[0]*x.shape[1], 1)

def vector_to_matrix(x):
    '''Convert a vector to a matrix'''
    return x.reshape(int(round(np.sqrt(x.shape[0]))),int(round(np.sqrt(x.shape[0]))))