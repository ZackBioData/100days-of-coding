# https://rosalind.info/problems/hamm/

from Bio import SeqIO
import os


# Get directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))
fasta_path = os.path.join(script_dir, "rosalind_hamm.fasta")
records = list(SeqIO.parse(fasta_path, "fasta"))

for i in range(len(records)):
    for j in range(i + 1, len(records)):
        # Calculate Hamming distance
        seq1 = records[i].seq
        seq2 = records[j].seq
        hamming_distance = sum(el1 != el2 for el1, el2 in zip(seq1, seq2))
        print(hamming_distance)