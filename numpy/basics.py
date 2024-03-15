import numpy as np # importing numpy



def basic_numpy_array():
    list = np.array([1, 2, 3, 4])

    print(list[0])
    print(list[1:])
    print(list[:-2])

    list[2] = 10
    print(list[2])


def basic_2d_array():
    multi_list = np.array([[1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, 11, 12]])
    print(multi_list[1])
    print(multi_list[2][1])

    print(multi_list.shape)
    print(multi_list.ndim) # number of dimensions
    print(multi_list.size)
    print(multi_list.dtype) # prints datatype


                          


#basic_numpy_array()
basic_2d_array()