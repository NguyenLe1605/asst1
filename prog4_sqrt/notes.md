1.  Speedup on SIMD-parallelization: 4x
    Speedup due to multi-core: 32x
    The output is as follow:

```bash
[sqrt serial]:          [639.042] ms
[sqrt ispc]:            [151.622] ms
[sqrt task ispc]:       [14.081] ms
                                (4.21x speedup from ISPC)
                                (45.38x speedup from task ISPC)

```

2. Changing the range of the input from [0, 3] to [0.001, 0.02], and the speed up is as follow.

```bash
[sqrt serial]:          [783.233] ms
[sqrt ispc]:            [143.377] ms
[sqrt task ispc]:       [12.127] ms
                                (5.46x speedup from ISPC)
                                (64.59x speedup from task ISPC)
```
    
    As we can see, compare to task 1 output, the running time of task iscp and sqrt ispc, although it does decrease, can not be compared to the increase in the running time of the serial version. This is due to the chosen range requires more iteration to converge. As the initial version chose the number randomly from a range that can have different number of iteration until converge, there will be small numbers that help the serial running time to go down. However, with the number of required iterations is higher, it causes the running time of the serial version to increase. In contrast, the running time of ispc and ispc task are still the same, hence increasing the overall speedup of the system. With each instances and gang in the ispc code handles roughly the same amount of work, but since each group of work is more fine-grained, making that the decrease in running time is not as big as the serial running time.

3. To minimize the speed up, I all input value to be 1.0. The performance is as follow:

```bash
[sqrt serial]:          [13.253] ms
[sqrt ispc]:            [9.738] ms
[sqrt task ispc]:       [10.743] ms
                                (1.36x speedup from ISPC)
                                (1.23x speedup from task ISPC)

```

- The reason of the loss in efficiency is also the reason I choose it. According to the initial graph, 1 costs nothing to converge, hence the serial version should be fast. These abstractions to parallelize will have synchronization and distribution cost internally that works well when the computation load is big, but with small computation, the serial version can move to the next task quickly, without having to pay some cost for internal synchonization. Hence, the running time so serial versio will match the ispc version.
