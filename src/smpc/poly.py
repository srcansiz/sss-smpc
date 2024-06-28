"""
Polynomial functions
"""
# Info
from typing import Tuple


# Adding a new comment here to explain ...

def extended_euclidian_alg(a, b) -> Tuple[int, int, int]:
    """Extended euclidean algorithm to find inverse of
    multiplicative inverse of a modulo b

    Args:
        b: Modulo base
        b: Divisor

    Return:
        GCD: greater common divisor of a and b
        x: Inverse of divisor
        y:
    """
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# Evaluates a polynomial

def evaluate_polynomial(coeffs, x):
    """Computes given polynomial function of given degree

    See: https://en.wikipedia.org/wiki/Polynomial

    Args:
        degree: Degree of the polynomial function from 1 to N
        x: Input of the function
    """
    f_x = [c * x**degree for degree, c in enumerate(coeffs)]
    return (x, sum(f_x))


# Adds comment galois poly

def galois_polynomial(
    coeffs,
    x,
    p
) -> int:
    """Computes galois filed polynomial of given input and coefficients

    Args:
        coeffs: Coefficients
        x: Input
        p: Prime number
    """
    return evaluate_polynomial(coeffs, x) % p

def lagrange_interpolation(
    x: int,
    k: int,
    j: int,
    nodes: Tuple[int]
) -> int:
    """Lagrange interpolation function

    Please see: https://en.wikipedia.org/wiki/Lagrange_polynomial

    Args:
        x: Interpolation value
        k: Polynomial degree
        j: Index of the current node
        nodes: Indices of all nodes
    """

    if not (k + 1) == len(nodes):
        raise ValueError(
            "The nodes number (numper of indexes) are not equal to ploynomial degree k-1 is "
        )

    result = 1

    for m in nodes:
        if m == j:
            continue
        result *= (x - m) / (j - m)


    return result

def extended_gcd_modular_integers(numerator, denominator):
    """Greatest common denominator"""
    old_r, r = numerator, denominator
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r , r = r, old_r - quotient * r
        old_s , s = s, old_s - quotient * s
        old_r , r = r, old_r - quotient * t

    return old_s, old_t



def mod_invers(k, prime):
    """Calculates numerator / denominator % p"""

    inv, _ = extended_gcd()


def lagrange_interpolate_gf(
    x,
    k,
    points: List[Tuple[int, int]],
) -> int:
    """Modular Lagrange Interpolate"""


    k = len(pints)

    def PI(values):
        result = 1
        for val in values:
            result *= val


    for point in points:

