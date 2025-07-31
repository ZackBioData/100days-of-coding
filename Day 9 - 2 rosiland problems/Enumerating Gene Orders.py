from itertools import permutations
import math

def main():
    n = 5
    # Print the total number of permutations (n!)
    print(math.factorial(n))
    # Generate and print each permutation of 1..n
    with open("rosalind_perm.txt", "w") as f:
        for perm in permutations(range(1, n+1)):
            f.write(" ".join(map(str, perm)) + "\n")
    print(f"All {math.factorial(n)} permutations written to {'rosalind_perm.txt'}")


main()
