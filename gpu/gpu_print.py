from numba import cuda

def cpu_print(N):
    for i in range(0, N):
        print(i)

@cuda.jit
def gpu_print(N):
    idx = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x 
    if (idx < N):
        print('idx = ', idx)

def main():
    print("gpu print:")

    # Must <= 1024, such as 16,32,128...
    threads_per_block = 4

    # if want 1000 threads, set blocks_per_grid = 128 and
    # threads_per_block = 1000/128 = 7.8 --> 8
    blocks_per_grid = 2

    gpu_print[blocks_per_grid, threads_per_block](5)
    cuda.synchronize()

    print("cpu print:")
    cpu_print(8)

if __name__ == "__main__":
    main()
