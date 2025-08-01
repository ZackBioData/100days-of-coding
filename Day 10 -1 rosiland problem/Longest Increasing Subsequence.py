#!/usr/bin/env python3
"""
Longest Increasing/Decreasing Subsequence via Dynamic Programming

We scan forward through each position `i` in the input permutation `pi`.
At each `i`, we look back at all earlier positions `j < i` and see whether we can
extend the best subsequence ending at `j` by adding `pi[i]`.

- We maintain `L_inc[i]`: length of the longest increasing subsequence ending at `i`.
- We maintain `P_inc[i]`: pointer to the previous index in that subsequence.

Specifically, for each `i`:
    for each `j < i`:
        if `pi[j] < pi[i]` and `L_inc[j] + 1 > L_inc[i]`:
            update `L_inc[i] = L_inc[j] + 1`
            record `P_inc[i] = j`

This reuses previously computed `L_inc[j]` values (never recomputing them)—
the hallmark of dynamic programming.  Once the tables are built, we find the
maximum `L_inc[i]`, backtrack via `P_inc` to reconstruct the actual subsequence,
and do the same for the decreasing case.
"""

def lis_and_lds(pi):
    n = len(pi)
    # L_inc[i]: best length of increasing subsequence ending at i
    # P_inc[i]: previous index in that subsequence
    L_inc = [1] * n
    P_inc = [-1] * n
    # Similarly for decreasing
    L_dec = [1] * n
    P_dec = [-1] * n

    # Build up subproblem solutions in a forward pass
    for i in range(n):
        # Look back at each earlier position j
        for j in range(i):
            # Can we extend an increasing subsequence?
            if pi[j] < pi[i] and L_inc[j] + 1 > L_inc[i]:
                L_inc[i] = L_inc[j] + 1  # update best length
                P_inc[i] = j            # record pointer for backtracking
            # Can we extend a decreasing subsequence?
            if pi[j] > pi[i] and L_dec[j] + 1 > L_dec[i]:
                L_dec[i] = L_dec[j] + 1
                P_dec[i] = j

    # Find the overall best lengths and their end positions
    max_inc_len = max(L_inc)
    end_inc = L_inc.index(max_inc_len)
    max_dec_len = max(L_dec)
    end_dec = L_dec.index(max_dec_len)

    # Backtrack to reconstruct the increasing subsequence
    inc_seq = []
    idx = end_inc
    while idx != -1:
        inc_seq.append(pi[idx])
        idx = P_inc[idx]
    inc_seq.reverse()

    # Backtrack to reconstruct the decreasing subsequence
    dec_seq = []
    idx = end_dec
    while idx != -1:
        dec_seq.append(pi[idx])
        idx = P_dec[idx]
    dec_seq.reverse()

    return inc_seq, dec_seq

# Example usage: read from a simple two-line file
if __name__ == "__main__":
    # First line: n, second line: space-separated permutation
    with open("rosalind_lgis.txt") as f:
        n = int(f.readline().strip())
        pi = list(map(int, f.readline().split()))
    inc, dec = lis_and_lds(pi)
    # Print results: increasing then decreasing
    print(" ".join(map(str, inc)))
    print(" ".join(map(str, dec)))
