import numpy as np
print("hello world")
def add_arrays(arr1, arr2):
    return np.add(arr1, arr2)

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
result = add_arrays(arr1, arr2)

print("Result:", result)