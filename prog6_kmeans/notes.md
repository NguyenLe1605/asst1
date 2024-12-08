- My measurement compute assignment runn

```bash
Running K-means with: M=1000000, N=100, K=3, epsilon=0.100000
[Compute Assignment Time]: 6116.998 ms
[Compute Centroids Time]: 1049.638 ms
[Compute Cost Time]: 1791.740 ms
[Total Time]: 8958.446 ms
```

- From this I believe if I optmize the compute assignment time to be at least 6x faster, I will achieve the performance.

- So to improve the performance, I start using threads to parallel the assignments works, resulting in a speedup of 2.5x. The idea is to have `NTHREADS` number of threads to handle a portion of the data vector. Each thread will handle `M / NTRHEADS` element. Different from the original code, realizing that checking all k elements first before the next element does not affect correctness, so I modify the order of computation to do kth check for each element then move to the next.

- The performance is now as follow:

```bash
[Compute Assignment Time]: 777.142 ms
[Compute Centroids Time]: 981.881 ms
[Compute Cost Time]: 1823.753 ms
[Total Time]: 3582.837 ms
```

- My code is as below:

```cpp
  std::thread threads[NTHREADS];
  int size = args->M / NTHREADS;
  for (int i = 0; i < NTHREADS; ++i) {
    threads[i] = std::thread([minDist, args, i, size] {
      int start = i * size;
      int end = start + size;
      for (int m = i * size; m < end; ++m) {
        for (int k = args->start; k < args->end; k++) {
          double d = dist(&args->data[m * args->N],
                          &args->clusterCentroids[k * args->N], args->N);
          if (d < minDist[m]) {
            minDist[m] = d;
            args->clusterAssignments[m] = k;
          }
        }
      }
    });
  }

```

- I improve the code further by putting the initialization of the array into the thread, and achieve nearly 2.6x speedup. The code is here

```cpp
void computeAssignments(WorkerArgs *const args) {
  double *minDist = new double[args->M];

  // Assign datapoints to closest centroids
  std::thread threads[NTHREADS];
  int size = args->M / NTHREADS;
  for (int i = 0; i < NTHREADS; ++i) {
    threads[i] = std::thread([minDist, args, i, size] {
      int start = i * size;
      int end = start + size;
      for (int m = i * size; m < end; ++m) {
        // init the array
        minDist[m] = 1e30;
        args->clusterAssignments[m] = -1;

        // Do the k loop to find the right assignment
        for (int k = args->start; k < args->end; k++) {
          double d = dist(&args->data[m * args->N],
                          &args->clusterCentroids[k * args->N], args->N);
          if (d < minDist[m]) {
            minDist[m] = d;
            args->clusterAssignments[m] = k;
          }
        }
      }
    });
  }
  for (auto &t : threads) {
    t.join();
  }

  free(minDist);
}
```

- The final performance:

```bash
Running K-means with: M=1000000, N=100, K=3, epsilon=0.100000
[Compute Assignment Time]: 750.930 ms
[Compute Centroids Time]: 970.826 ms
[Compute Cost Time]: 1666.763 ms
[Total Time]: 3388.581 ms
```

