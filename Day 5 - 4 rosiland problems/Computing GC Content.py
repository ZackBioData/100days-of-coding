# https://rosalind.info/problems/gc/

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
import os


records = list(SeqIO.parse("rosalind_splc.fasta", "fasta"))


# Track highest GC content and ID
max_gc = 0
max_id = ""
# Loop over each record and calculate GC content
for record in records:
    gc = gc_fraction(record.seq) * 100  # get % value
    if gc > max_gc:
        max_gc = gc
        max_id = record.id

# Print results
print(max_id)
print(f"{max_gc:.6f}")