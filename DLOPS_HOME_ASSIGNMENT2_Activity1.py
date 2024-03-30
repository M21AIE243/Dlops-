# -*- coding: utf-8 -*-
"""DLOPS_HOME_ASSIGNMENT2__Activity1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m9bb1D1_w7CM7RDU-G_6r3W6WahI1p2f
"""

import numpy as np
import matplotlib.pyplot as plt

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ReLU function
def relu(x):
    return np.maximum(0, x)

# Leaky ReLU function
def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

# Tanh function
def tanh(x):
    return np.tanh(x)

# Generate x values
x = np.linspace(-5, 5, 100)

# Generate y values for each activation function
y_sigmoid = sigmoid(x)
y_relu = relu(x)
y_leaky_relu = leaky_relu(x)
y_tanh = tanh(x)

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y_sigmoid, label='Sigmoid', color='blue')
plt.title('Sigmoid')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x, y_relu, label='ReLU', color='orange')
plt.title('ReLU')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x, y_leaky_relu, label='Leaky ReLU', color='green')
plt.title('Leaky ReLU')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x, y_tanh, label='Tanh', color='red')
plt.title('Tanh')
plt.legend()

plt.tight_layout()
plt.show()

"""2. a. In the "feature-1" branch, create a new file to print sigmoid for the
following data and commit changes:
random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]
"""

random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]


for value in random_values:
    print(f"Sigmoid of {value}: {sigmoid(value)}")

"""2. b. In the "feature-2" branch, modify an existing file to print the output when
ReLU, Leaky ReLU, and Tanh are applied to the same data and commit changes.
"""

import numpy as np

random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]

# def relu(x):
#     return np.maximum(0, x)

# def leaky_relu(x, alpha=0.01):
#     return np.where(x > 0, x, alpha * x)

# def tanh(x):
#     return np.tanh(x)

print("ReLU:")
print([relu(value) for value in random_values])
print("\nLeaky ReLU:")
print([leaky_relu(value) for value in random_values])
print("\nTanh:")
print([tanh(value) for value in random_values])

"""2. c. In the "bug-fix" branch, fix an issue introduced in one of the previous
branches.
"""

