"""Run Experiment 1 and save every trial in results/exp1_birthday.csv.

Usage (from the root of the repository):
    python src/run_exp1.py
"""

import csv
import os

from birthday import HASH_FUNCTIONS, expected_attempts, find_collision

SIZES=[16, 20, 24, 28, 32]        # numbers of bits kept
NB_TRIALS=100                     # trials per (function, size)
OUTPUT="results/exp1_birthday.csv"


def main():
    os.makedirs("results", exist_ok=True)

    with open(OUTPUT, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["function", "n", "trial", "attempts", "seconds","msg1_hex", "msg2_hex"])

        for n in SIZES:
            for name in HASH_FUNCTIONS:
                all_attempts = []

                for trial in range(1, NB_TRIALS + 1):
                    # the trial number is the seed : different for each trial but reproducible
                    attempts,duration, m1, m2 = find_collision(name, n, trial)
                    all_attempts.append(attempts)
                    writer.writerow([name, n, trial, attempts, duration,m1.hex(), m2.hex()])

                mean=sum(all_attempts)/len(all_attempts)
                theory=expected_attempts(n)
                print(f"n={n}  {name:9}  mean={mean:.0f}  theory={theory:.0f}  ratio={mean / theory:.2f}")

    print(f"CSV saved in {OUTPUT}")


if __name__ == "__main__":
    main()