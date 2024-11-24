- Hypothesize: the perfomance of the program will increase as a linear function of thread.
    - For view 2, the performance is indeed a linear function of thread, however it's not close 16x as I expected.
    - For view 1, the performance is still somewhat linear, but the graph plummets at 3 threads, the increase again. The graph is not smooth.

- Observation:
    - View 2: smoothly increase as a linear function of thread.
    - View 2:
        plummet at thread 3.
        Increase from thread 3
            - t4 is faster than t3
            - The graph show the increase from thread 4 to thread 12 is not smooth, but gradually turns to smooth
            - Then from 12 to 15: the line is straight
            - At final 16 threads, it increase upward.
    - Assumption:
        - Work on the main thread then join, as the running of task on the main thread, is after on the other thread then it tries to join. If the main thread starts later
        than any other spawned thread, making the time to join on the finished work is much later then it would be parallel.
        In the 3-thread case, it could be that, the latency to wait for main thread is too high, causing the whole system to be slow down.
        For the 4-thread case, the unit of of work is smaller, making the processing faster, hence the latency for the final join is reduced.
    - Why the thread is linear: more thread, the unit of work for each thread is smaller, hence the time for processing one unit of work should be faster. The unit of work
    - After review from PKU ideas: the problem couble the distribution of work, as we can see on the image. For image 1, most of the computation is in the middle area, while
    the area to the top and bottom rear required less heavy computation. While at the image 2, the computation on the image 2 is more heavy at the front rows, but less at the bottom rows.

    This can be seen at the measurment of running time for each work.

    for example at 3 threads, both view points.

    view 1

    ```bash
    ❯ ./mandelbrot -t 3
    [mandelbrot serial]:            [379.663] ms
    Wrote image file mandelbrot-serial.ppm
            [mandelbrot thread measure - 0 - nrows: 400]:           [76.144] ms
            [mandelbrot thread measure - 2 - nrows: 400]:           [76.619] ms
            [mandelbrot thread measure - 1 - nrows: 400]:           [237.056] ms
            [mandelbrot thread measure - 0 - nrows: 400]:           [79.839] ms
            [mandelbrot thread measure - 2 - nrows: 400]:           [80.466] ms
            [mandelbrot thread measure - 1 - nrows: 400]:           [239.162] ms
            [mandelbrot thread measure - 0 - nrows: 400]:           [76.588] ms
            [mandelbrot thread measure - 2 - nrows: 400]:           [77.870] ms
            [mandelbrot thread measure - 1 - nrows: 400]:           [237.599] ms
            [mandelbrot thread measure - 0 - nrows: 400]:           [76.763] ms
            [mandelbrot thread measure - 2 - nrows: 400]:           [77.183] ms
            [mandelbrot thread measure - 1 - nrows: 400]:           [237.010] ms
            [mandelbrot thread measure - 0 - nrows: 400]:           [77.611] ms
            [mandelbrot thread measure - 2 - nrows: 400]:           [77.883] ms
            [mandelbrot thread measure - 1 - nrows: 400]:           [236.826] ms
    [mandelbrot thread]:            [237.035] ms
    Wrote image file mandelbrot-thread.ppm
                                    (1.60x speedup from 3 threads)
    ```

    view 2

    ```bash
    ❯ ./mandelbrot -t 3 --view 2
    [mandelbrot serial]:            [234.794] ms
    Wrote image file mandelbrot-serial.ppm
            [mandelbrot thread measure - 2 - nrows: 400]:           [63.079] ms
            [mandelbrot thread measure - 1 - nrows: 400]:           [68.585] ms
            [mandelbrot thread measure - 0 - nrows: 400]:           [108.045] ms
            [mandelbrot thread measure - 2 - nrows: 400]:           [63.234] ms
            [mandelbrot thread measure - 1 - nrows: 400]:           [68.601] ms
            [mandelbrot thread measure - 0 - nrows: 400]:           [107.812] ms
            [mandelbrot thread measure - 2 - nrows: 400]:           [63.323] ms
            [mandelbrot thread measure - 1 - nrows: 400]:           [68.526] ms
            [mandelbrot thread measure - 0 - nrows: 400]:           [107.655] ms
            [mandelbrot thread measure - 2 - nrows: 400]:           [63.333] ms
            [mandelbrot thread measure - 1 - nrows: 400]:           [68.610] ms
            [mandelbrot thread measure - 0 - nrows: 400]:           [107.767] ms
            [mandelbrot thread measure - 2 - nrows: 400]:           [63.231] ms
            [mandelbrot thread measure - 1 - nrows: 400]:           [68.660] ms
            [mandelbrot thread measure - 0 - nrows: 400]:           [107.926] ms
    [mandelbrot thread]:            [107.726] ms
    Wrote image file mandelbrot-thread.ppm
                                    (2.18x speedup from 3 threads)
    ```

    The result of this measurement somewhat confirm at view1, the computation is heavier in the middle, while the computation is heavier at the top view 2.

