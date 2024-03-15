import numpy as np

a = np.array([[1, 2, 3, 4],
             [4, "hello", 5, 7],
             [8, 9, 10, 11]])

print(a.size)
print(a.shape)
print(a.ndim)
print(a.dtype)

print(type(a[1][2]))

#can set datatype by passing dtype arguement
#EG: a = np.array([1,2,3,4], dtype=np.float32)

