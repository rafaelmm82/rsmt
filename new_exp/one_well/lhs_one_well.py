from doepy import build
from math import ceil
import numpy as np

import matplotlib.pyplot as plt

one_well = {
    'x': [1, 14],
    'y': [1, 26],
    'z': [2, 15],
}

# 312 é o mmc entre os ranges de indíces
lhs = build.lhs(d=one_well, num_samples=20)
lhsf = lhs.apply(np.floor)
lhs.plot.hist(bins=312, alpha=0.5)
plt.show()
lhsf.plot.hist(bins=312, alpha=0.5)
plt.show()

lhsf.describe()

lhsf.astype(int)


     x   y   z
0    9  10   5
1    9  23  12
2    1  16   2
3    2  12   3
4    2   4   5
5    5   6  14
6    4  23   9
7   10  17  10
8   11  19  10
9    3   9  14
10   7   3   7
11   8  18   2
12  13  13   7
13  12   3   6
14   7  12  12
15   6   7  11
16  12  24   8
17   3  15  13
18   5   2   9
19  10  21   4



for n, pos in enumerate(lhsf.values.astype(int)):
    print(f"WELL 'Producer_{n+1:02d}'  VERT {pos[0]} {pos[1]} ATTACHTO 'ALL-WELLS'")
    print(f"PRODUCER 'Producer_{n+1:02d}'")
    print(f"OPERATE  MIN  BHP  1000.0  CONT")
    print(f"GEOMETRY  K  0.5  0.355  1.0  0.0")
    print(f"PERF       GEO  'Producer_{n+1:02d}'")
    print(f"{pos[0]} {pos[1]} {pos[2]}         1.0  OPEN    FLOW-TO  'SURFACE'  REFLAYER")
    print("\n")




WELL  'Producer_01'  VERT  8  2 ATTACHTO 'ALL-WELLS'
PRODUCER 'Producer_01'
OPERATE  MIN  BHP  1000.0  CONT
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.5  0.355  1.0  0.0  
PERF       GEO  'Producer_01'
** UBA             ff          Status  Connection  
8 2 2         1.0  OPEN    FLOW-TO  'SURFACE'  REFLAYER
