# signed_perm.py

import itertools  # for permutations and sign combinations
import math

def main():
    n = 3
    numbers = list(range(1, n + 1))
    output_path = "signed_permutations.txt"

    with open(output_path, "w") as f:
        # Total number of signed permutations: n! * 2^n
        total = math.factorial(n) * (2 ** n)
        f.write(f"{total}\n")

        # Generate and write each signed permutation
        for perm in itertools.permutations(numbers): # all orderings of [1..n]
        # --- inner product factor: all sign vectors of length n (2^n of them) ---
            for sign_choice in itertools.product([1, -1], repeat=n):
                signed_perm = [sign_choice[i] * perm[i] for i in range(n)]
                # Format with explicit plus sign for positives
                line = " ".join(f"{'+' if x > 0 else ''}{x}" for x in signed_perm)
                f.write(line + "\n")

    print(f"Wrote {total} signed permutations to {output_path}")

# Immediately run
main()
