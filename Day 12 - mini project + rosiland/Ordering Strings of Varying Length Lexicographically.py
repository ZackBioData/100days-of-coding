from itertools import product

alphabet = ['J', 'E', 'V', 'Z', 'N', 'W', 'B', 'P', 'G', 'H', 'A', 'L']
max_Length = 4
output_path = "Lexicographic_kmers.txt"
def expand(prefix, depth, out):
    if depth > max_Length:
        return
    if prefix:  # skip writing empty prefix
        out.write(prefix + "\n")
    for letter in alphabet:
        expand(prefix + letter, depth + 1, out)

with open(output_path, "w") as out:
    for letter in alphabet:
        expand(letter, 1, out)

