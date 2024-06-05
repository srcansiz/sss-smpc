"""Random module"""

import random

def generate_random():
    """Generated random integer using prime number"""

    p = 0
    while p == 0:

        # To keep the random values in range not too high
        # we are taking mod with a prime number around 1000
        p = random.randint(0, 1000) % 997
    return p
