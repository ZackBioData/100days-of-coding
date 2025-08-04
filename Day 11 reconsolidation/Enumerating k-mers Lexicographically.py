from itertools import product

alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
Length = 3

# Sort the alphabet just in case it's not already
alphabet = sorted(alphabet)

# Generate lexicographic kmers
for kmer in product(alphabet, repeat=Length):
    print("".join(kmer))