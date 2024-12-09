1. Performance:

```bash
❯ ./saxpy --help
[saxpy ispc]:           [11.901] ms     [25.041] GB/s   [3.361] GFLOPS
[saxpy task ispc]:      [14.450] ms     [20.624] GB/s   [2.768] GFLOPS
                                (0.82x speedup from use of tasks)

```

For the ISPC tasks, there is no speedup from ISPC, only degrade in the running time. The hypothesis is the limited bandwidth can not satisfy the number of CPUs. Since we are loading huga amount of data here for each CPU core, the memory bandwith may not provide the each core the data at the same rate as the single-core case. Now each core will handless less data at a time, combining with more iteration of running, and the runtime overhead, this can cause the overall performance to reduce. The performance of the program can be substantially increased with better reogranizing data accessing pattern to reduce the overhead of loading data from memory, helping the traffic is now crowded during the load of data.

2. The total memory bandwidth is `TOTAL_BYTES = 4 * N * sizeof(float)`. The operations causing memory operations are as follow:
    - A load of an element from X.
    - A load of an element from Y.
    - If the element from result is missed, a load for variable `result` from memory to the cache are required.
    - A store from result.

Hence, the multiplier by 4 for the total memory bandwidth formula is correct.
