# https://rosalind.info/problems/gc/

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
import os


# Get directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))
fasta_path = os.path.join(script_dir, "rosalind_gc.fasta")

records = list(SeqIO.parse(fasta_path, "fasta"))

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