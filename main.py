def best_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)  # To store allocations

    for i, process in enumerate(process_sizes): #iterating each process one by one
        best_idx = -1  # Initialize the best-fit index
        for j, block in enumerate(block_sizes):
            if block >= process:
                if best_idx == -1 or block_sizes[j] < block_sizes[best_idx]:
                    best_idx = j
        if best_idx != -1:  # Allocate process
            allocation[i] = best_idx #allocation of 'i'th process
            block_sizes[best_idx] -= process #reducing the size of block allocated

    return allocation

# Example Usage
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112]
allocations = best_fit(blocks, processes)
print("Allocations:", allocations)



