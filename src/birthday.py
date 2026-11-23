"""Experiment 1 - Birthday attack on truncated hashes
 
The experiment itself is in run_exp1.py.
"""

import hashlib
import random
import time
import math

HASH_FUNCTIONS = ["md5", "sha1", "sha256", "sha3_256"]


def truncate(digest, nb_bits):
    """Keep only the first nb_bits of a digest (bytes) as an integer."""
    hash_bits= len(digest)*8
    number = int.from_bytes(digest, "big")
    return number >> (hash_bits - nb_bits)


def find_collision(hash_name, nb_bits, seed):
    """Try random 16-byte messages until two different ones have the same
    first nb_bits of hash.
 
    Returns (attempts, duration in seconds, message 1, message 2).
    The same seed always gives the same result (reproducibility).
    """
    rng = random.Random(seed)
    seen = {}   # truncated hash => message that produced it
    attempts=0
    start=time.perf_counter()

    while True:
        msg = rng.randbytes(16)
        attempts+=1
        value=truncate(hashlib.new(hash_name, msg).digest(),nb_bits)

        if value in seen and seen[value] != msg:
            duration=time.perf_counter()-start
            return attempts, duration, seen[value], msg

        seen[value]=msg


def expected_attempts(nb_bits):
    """Theoretical mean number of tries before the first collision:
    sqrt(pi * 2^n / 2), about 1.25 * 2^(n/2) (Equation (2) of the report)."""
    return math.sqrt(math.pi*2**nb_bits/2)