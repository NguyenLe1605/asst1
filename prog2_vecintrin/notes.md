- Vector width:
    2:

    Results matched with answer!
****************** Printing Vector Unit Statistics *******************
Vector Width:              2
Total Vector Instructions: 17123
Vector Utilization:        77.8%
Utilized Vector Lanes:     26654
Total Vector Lanes:        34246
************************ Result Verification *************************
Passed!!!

4: 

Results matched with answer!
****************** Printing Vector Unit Statistics *******************
Vector Width:              4
Total Vector Instructions: 9919
Vector Utilization:        70.6%
Utilized Vector Lanes:     28016
Total Vector Lanes:        39676
************************ Result Verification *************************
Passed!!!

8:

CLAMPED EXPONENT (required)
Results matched with answer!
****************** Printing Vector Unit Statistics *******************
Vector Width:              8
Total Vector Instructions: 5457
Vector Utilization:        66.5%
Utilized Vector Lanes:     29020
Total Vector Lanes:        43656
************************ Result Verification *************************
Passed!!!

16:
Results matched with answer!
****************** Printing Vector Unit Statistics *******************
Vector Width:              16
Total Vector Instructions: 2861
Vector Utilization:        64.9%
Utilized Vector Lanes:     29700
Total Vector Lanes:        45776
************************ Result Verification *************************
Passed!!!

- What I observe is the as the `VECTOR_WIDTH` increases, the vector utilization decreases. The total vector instructions decrease nearly in half for each double of the vector width. For the decrease of the vector utilization, we can observe that the utilized vector lanes does not change as the number of vector lanes change. The reason could lie on my implementation of the exponential calculation. For each loop of multiplying the value, if there is a really big number of exponent comparing to other exponent, the bigger one will cause other vector lane to do nothing, while waiting for the bigger one to finish its work. With the values are the same of each `VECTOR_WIDTH`, with larger number of `VECTOR_WIDTH`, the large number will still affect the number surrounding, even if there are more chances of more who are closed to it, the small number around will cause the vector lane are not fully utilized.

