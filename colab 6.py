from sklearn.linear_model import Lasso
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

# We'll again use the digit dataset to demonstrate the effect of choosing \lambda
dataset = datasets.load_digits()

# We split our data into training and validation, the split here is arbitray
x_train = dataset.data[:450]
y_train = dataset.target[:450]
x_val = dataset.data[450:]
y_val = dataset.target[450:]


import pandas as pd
from sklearn import linear_model
import random

def gradientDesc(weights, X, y, train_len, alpha, learning_rate, n_iter):
    """
    Args:
        weights : shape (n,1)
        X : shape (m, n)
        y : shape (m, 1)
        train_len : # of training samples
        alpha : regularization parameter
        learning_rate : learning rate of the weights
        n_iter = # of iteration
    Returns:
        weights : the updated weights vector
    """
    for i in range(n_iter):

        derivation = - 2 * np.dot(X.T, y - np.dot(X, weights)) + 2 * alpha * weights

        weights -= learning_rate * derivation / train_len

        ######### Your Turn  #########
        #
        # Write your own code here
        #
        ## Update the weights here
        #
        ##############################

    return weights


alpha = 1
learning_rate = 0.5
n_iter = 1500

diabetes = datasets.load_diabetes()
diabetes_X_raw = diabetes.data
print("NUMBER OF FEATURES: ", diabetes_X_raw.shape[1])

# Concatenate 1 to each sample to match with the bias term
diabetes_X = np.array(list(map(lambda x: np.concatenate(([1], x)), diabetes_X_raw)))

# Use 100 samples for test set.
train_x = diabetes_X[:-100]
test_x = diabetes_X[-100:]
train_y = diabetes.target[:-100]
test_y = diabetes.target[-100:]

train_len = train_x.shape[0]
weights = [0.0] * (train_x.shape[1])  # Weights or parameter vector initialized with 0
weights = np.array(weights)

# To train on train data set
weights = gradientDesc(weights, train_x, train_y, train_len, alpha, learning_rate, n_iter)

# Even though we optimized the weights on MSE with regularization error, we use Mean Absolute Percentage Error as test metric,
residuals = np.sum(np.array(test_x) * weights, axis=1) - test_y
residuals = [(abs(a) / b) * 100 for a, b in zip(residuals, test_y)]
cost = sum(residuals) / len(residuals)

print('Mean Absolute Percentage Error of our Model on test set:', cost, '%')