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
With `mandelbrot_ispc` and the parameter `--tasks`, on view 1, I saw the speedup to be 6.85x, which 2x faster compare to the ISPC without tasks.

