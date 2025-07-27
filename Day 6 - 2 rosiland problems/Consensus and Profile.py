from Bio import SeqIO
from collections import Counter, defaultdict

records = list(SeqIO.parse("rosalind_cons1.fasta", "fasta"))
full_dna = list(zip(*[str(record.seq) for record in records]))


profile = {
    'A': [],
    'C': [],
    'G': [],
    'T': []
}

for col in full_dna:
    counts = Counter(col)
    for base in "ACGT":
        profile[base].append(counts.get(base, 0))

consensus = ""
for i in range(len(full_dna)):
    max_base = max("ACGT", key=lambda base: profile[base][i])
    consensus += max_base

print(consensus)