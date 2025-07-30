from Bio import SeqIO

def get_substrings(s):
    """
    Generate all possible substrings of the input string s,
    returning them from longest to shortest.

    Parameters:
        s (str): The string from which to generate substrings.

    Returns:
        List[str]: A list of every substring of s, ordered by decreasing length.
    """
    substrs = []             # Will hold all substrings
    n = len(s)               # Total length of the string

    # For each possible substring length L from n down to 1
    for L in range(n, 0, -1):
        # Slide a window of length L along the string
        # i goes from 0 up to n - L
        for i in range(n - L + 1):
            # Extract the substring of length L starting at i
            substrs.append(s[i:i + L])
    return substrs          # Return all substrings, longest first

def longest_common_substring_bruteforce(records):
    """
    Find the longest substring common to all sequences in the provided SeqRecord list,
    using a brute‑force approach.

    """
    # Convert each SeqRecord to a plain Python string
    seqs = [str(rec.seq) for rec in records]

    # Sort by length so the shortest sequence is first
    # We only need to generate substrings from the shortest one
    seqs.sort(key=len)
    shortest = seqs[0]       # The sequence to pull substrings from
    others = seqs[1:]        # The rest of the sequences

    # Generate substrings from longest to shortest
    for sub in get_substrings(shortest):
        # Check if this substring appears in every other sequence
        if all(sub in seq for seq in others):
            return sub       # As soon as one matches all, it's the LCS

    return ""  # If no common substring is found (edge case), return empty




if __name__ == "__main__":
    # Parse the FASTA file (make sure the filename matches exactly)
    records = list(SeqIO.parse("rosalind_lcsm (2).fasta", "fasta"))

    # Compute the longest common substring
    result = longest_common_substring_bruteforce(records)

    # Output the result
    print("Brute‑force LCS:", result)
