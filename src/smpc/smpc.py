import uuid
import functools

from typing import Callable
from .poly import evaluate_polynomial
from .random import generate_random

class ShamirShare:
    """Class to keep share of a secret"""

    def __init__(
        self,
        index:int,
        share: int,
        k: int,
        p: int,
    ) -> None:
        """Constructs Shamir's share

        Args:
            index: Party/share index
            share: Share value
            k: Polynomial degree used for creating share
            p: Prime number used for Galois Field.

        Returns:
            None
        """


        self.index = index
        self.share = share
        self.k = k
        self.prime = p


class SecretConstructor:
    """Constructs secret by collecting the shares from parties

    """

    def __init__(
        self,
        shares: List[ShamirShare],
        prime: None | int = None
    ):
        self.shares = shares

    def build(self):
        """Build secret by given shares"""


        def PI(x):
            pass


        r = 1

        for m, share in enumerate(self.shares):
            if not
                r *= share.index



class ShamirSecretHolder:
    """MPC Party"""

    def __init__(self, secret, id = None):
        """Party constructor"""
        self._id = id or uuid.uuid1()
        self._secret = secret
        self._poly: Callable = None

    def share(self, i, k):
        """Create single share of secret for given share index

        Share function creates a callable polynomial function as degree of k

        Args:
            i: Share index
            k: Degree of Polynomial function that is going to be created.
        """
        if i <= 0:
            raise ValueError(
                "Share index `x`, also input of Polynomial function should "
                "be non-negative and non-zero.")

        if not self._poly:
            self._poly = self._create_polynomial_function(k)

        return self._poly(x=i)

    def shares(self, n, k):
        """Returns shares for each party

        Args:
            n: Number of shares to generate.
            k: Degree of Shamir's secret sharing Polynomial function. It also indicates
                that `k+1` is the minimum number of parties that can construct secret
                together.
        """

        shares = [self.share(i,k) for i in range(1, n+1)]
        return shares


    def _create_polynomial_function(self, degree):
        """Generates share for single party

        Args:
            degree: Degree of polynomial function

        Returns:
            A callable polynomial function
        """

        coeffs = [generate_random() for _ in range(degree)]
        coeffs = [self._secret, *coeffs]

        return functools.partial(evaluate_polynomial, coeffs=coeffs)

