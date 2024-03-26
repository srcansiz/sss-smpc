

import numpy as np
import math



secret = 1234

func = "x^2 + y + secret"


r1 = math.random(1,100)
r2 = math.random(1,100)


funct_value = r1**2 + r2** + secret



def theate_i(x, i, k):
    """SSS Theate function"""

    if j == i:
        raise ValueError("j can not be equal to i")

    x = 1
    for j in range(1, k+1):
        if j == i:
            continue
        x *= (x - i) / (i - j)

    return j
