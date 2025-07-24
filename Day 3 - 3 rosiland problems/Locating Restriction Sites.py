from Bio import SeqIO

def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

# Read the sequence from FASTA
record = SeqIO.read("rosalind_revp.fasta", "fasta")  # Replace with your filename
seq = str(record.seq)

# Search for reverse palindromes
for i in range(len(seq)):
    for l in range(4, 13):  # lengths from 4 to 12
        sub = seq[i:i+l]
        if len(sub) < l:
            continue
        if sub == reverse_complement(sub):
            print(i+1, l)  # 1-based index
