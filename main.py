import torch
import numpy as np

x = torch.rand(2, 3)
print("This is the result of torch.rand(2, 3):\n", x)

'''
Tensors are a specialized data structure that are very similar to arrays and matrices. In PyTorch, we use tensors to encode the inputs and outputs of a model, as well as the model’s parameters.
'''

# Tensors can be initialized in various ways. Take a look at the following examples:

# 1. Tensors can be created directly from data. The data type is automatically inferred.

data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)

# 2. Tensors can be created from NumPy arrays

np_array = np.array(data)
x_np = torch.from_numpy(np_array)

print("Tensor 1: ", x_data)
print("Tensor 2: ", x_np)