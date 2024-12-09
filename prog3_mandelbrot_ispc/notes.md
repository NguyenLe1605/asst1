CPU - info:
    - 6 cores
    - Each core has 2 threads.
What is the maximum speedup you expect given what you know about these CPUs?
- Given that the CPU core used the 8-wide AVX2 vector instructions, I expect the program to give at least 7x-8x speedup for the program. But in reality, the speedup was around 3.5x for view 1, and 2.8x for view 2.
Why might the number I observe be less than this ideal?
    - Consider the characteristics of the computation I am performing.
        - The work distribution is not fair for different part of the image.
        - The workload is denser in the middle, and more spreaded in the rear view. For view 2, the work high density work load is thin, causing the calculations of 8 unit around a high density entry is dominated by the dense entry. And with the calculation is more spread, the speed up will not as good as view 1, with the high computation are close to each other, really efficient for vectorize instruction.
        - The parts of the images that present challenges are the parts that are moving from a black area into the small grey area, or the grey area into the white area. Since the SIMD calculation of the white part will cause the whole SIMD calcuation to compute slower.
        - One other thing to consider, is the way of choosing to map the task. With for_each for the height outside, it may not take advantage of the fact the closer the entry in a row, the better they are close to the average workload.

1. With `mandelbrot_ispc` and the parameter `--tasks`, on view 1, I saw the speedup to be 6.85x, which 2x faster compare to the ISPC without tasks.
2. For the number of tasks, I choose 32. At number 64, the answer is incorrect. The process of determine the number of tasks to create: with the speedup of the ispc tasks are already 4-5x, roughly 7x-8x performance needs to be achieve from ISPC to get over 32x perf, on the experiment for each number from 8 to 32, the number 32 is the only one that can pass the 32x threshold.
    Why does the number 32 work the best?
        1. It's the maximum number that matches the performance + correctness. For performance, with the number of threads are 16, the runtime of the ISPC schedule 32 threads well enough to meet the speedup.
        2. With the workload distrubtion of the image is not fair, a number that is more fine-grained to divide up the tasks into smaller region where, the workload are close to each other can help the vectorized instructions acts on closer entry => workload is distributed more fairly.

3. For the ISPC task abstraction, this abstraction involves an runtime with a thread pool of worker threads. To launch a task is to put a task into some shared space and the threads inside the runtime will try to claim the task and work on it. Different from a ISPC task, a thread will not try to claim any work but do the assigned works for the thread until the end of its lifetime.

