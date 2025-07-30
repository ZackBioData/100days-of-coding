import math

def independent_assortment(k: int, N: int) -> float:
    """
    Calculate the number of pairs of rabbits after n generations,
    given that each pair produces k pairs of offspring.

    Parameters:
        k (int): Number of generations
        n (int): Number of Aa Bb after k generations.
        Each pair produces 2 pairs of offspring all parents have Aa Bb genotype

        math
         p = 1/4            # success probability for Aa Bb

    Returns:
        the probability n (total number of Aa Bb pairs after k generations.)   
        We model the number of Aa Bb offspring as Binomial(n=2**k, p=1/4),
        and return P(X ≥ N).

        we are calculating the belcurve of proabiltiy of having at least n Aa Bb pairs
        after k generations.
       """
    n = 2**k           # total children in generation k
    p = 1/4            # success probability for Aa Bb

    # Sum binomial probabilities from N to n
    prob = 0.0
    for i in range(N, n+1):
        prob += math.comb(n, i) * p**i * (1-p)**(n-i)
    return prob

if __name__ == "__main__":
    # Read input: two integers k and N
    k = 5
    N = 8
    result = independent_assortment(k, N)
    # Print with 6 decimal places per Rosalind format
    print(f"{result:.6f}")