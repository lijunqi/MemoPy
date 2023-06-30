import numpy as np
from numba import cuda

@cuda.jit
def increment_by_one(an_array):
    # Thread id in a 1D block
    tx = cuda.threadIdx.x
    # Block id in a 1D grid
    ty = cuda.blockIdx.x
    # Block width, i.e. number of threads per block
    bw = cuda.blockDim.x
    # Compute flattened index inside the array
    pos = tx + ty * bw
#    print('tx = %s, ty = %s' % (tx, ty))
    if pos < an_array.size:  # Check array boundaries
        an_array[pos] += 1


lst = np.array([1,2,3])

threadsperblock = 32
blockspergrid = (lst.size + (threadsperblock - 1)) // threadsperblock

increment_by_one[blockspergrid, threadsperblock](lst)
print(lst)
