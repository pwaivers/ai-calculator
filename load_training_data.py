import numpy as np 

from sklearn.model_selection import train_test_split

# Creates size-n^2 training data set of a + b for a,b from 0 to n-1
def load_plus_training_data(n):
    a, b = np.meshgrid(np.arange(n), np.arange(n))
    x_data = np.vstack([a.flatten(), b.flatten()]).T
    y_data = np.sum(x_data, axis=1)
    return train_test_split(x_data, y_data)

# Creates size-n^2 training data set of a - b for a,b from 0 to n-1
def load_minus_training_data(n):
    a, b = np.meshgrid(np.arange(n), np.arange(n))
    x_data = np.vstack([a.flatten(), b.flatten()]).T
    y_data = x_data[:, 0] - x_data[:, 1]
    return train_test_split(x_data, y_data)

# Creates size-n^2 training data set of a * b for a,b from 1 to n
def load_multiply_training_data(n):
    a, b = np.meshgrid(np.arange(1, n+1), np.arange(1, n+1))
    x_data = np.vstack([a.flatten(), b.flatten()]).T
    y_data = x_data[:, 0] * x_data[:, 1]
    return train_test_split(x_data, y_data)

# Creates size-n^2 training data set of a / b for a,b from 1 to n
def load_divide_training_data(n):
    a, b = np.meshgrid(np.arange(1, n+1), np.arange(1, n+1))
    x_data = np.vstack([a.flatten(), b.flatten()]).T
    y_data = x_data[:, 0] / x_data[:, 1]
    return train_test_split(x_data, y_data)

def load_training_data(n, method="plus"):
    if method == "plus":
        return load_plus_training_data(n)
    elif method == "minus":
        return load_minus_training_data(n)
    elif method == "multiply":
        return load_multiply_training_data(n)
    elif method == "divide":
        return load_divide_training_data(n)
    else:
        raise NotImplementedError
