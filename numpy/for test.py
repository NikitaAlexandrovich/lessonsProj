import numpy as np
# 12. Create a 3x3x3 array with random values (★☆☆)
array_rand_val = np.random.random((3, 3, 3))
print(array_rand_val)


# 34. How to get all the dates corresponding to the month of July 2016? (★★☆)
arr = np.arange('2016-07', '2016-08', dtype='datetime64[D]')

print(arr)


# 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)
rr = [1,2,3,4,5,6]

I = [1,3,9,3,4,1]

ft = np.bincount(I,rr)

print(ft)
