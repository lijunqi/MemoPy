from numba import cuda, float32
import numpy as np

# Controls threads per block and shared memory usage.
# The computation will be done on blocks of TPBxTPB elements.
TPB = 4

@cuda.jit
def fast_matmul(A, B, C):
    # Define an array in the shared memory
    # The size and type of the arrays must be known at compile time
    sA = cuda.shared.array(shape=(TPB, TPB), dtype=float32)
    sB = cuda.shared.array(shape=(TPB, TPB), dtype=float32)

    x, y = cuda.grid(2)

    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    bpg = cuda.gridDim.x    # blocks per grid


    if x >= C.shape[0] and y >= C.shape[1]:
        # Quit if (x, y) is outside of valid C boundary
        return

    # Each thread computes one element in the result matrix.
    # The dot product is chunked into dot products of TPB-long vectors.
    tmp = 0.
    for i in range(bpg):
        print(x, ty, i, TPB, tx, i, TPB, y)
        # Preload data into shared memory
        sA[tx, ty] = A[x, ty + i * TPB] # row
        sB[tx, ty] = B[tx + i * TPB, y] # col

        # Wait until all threads finish preloading
        cuda.syncthreads()

        # Computes partial product on the shared memory
        for j in range(TPB):
            tmp += sA[tx, j] * sB[j, ty]

        # Wait until all threads finish computing
        cuda.syncthreads()

#    print(x,y, tmp)
    C[x,y] = tmp



threads_per_block = (TPB,TPB)
blocks_per_grid = (2,2)

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13,14,15,16]], dtype=np.float)
B = np.array([[11, 12, 13, 1], [14, 15, 16,1], [17, 18, 19,1], [20, 21, 22, 1]], dtype=np.float)
C = np.zeros((4,4))
print(C.shape)

fast_matmul[blocks_per_grid, threads_per_block](A, B, C)

cuda.synchronize()

print(C)
