#https://rosalind.info/problems/orf/
from Bio import SeqIO
from Bio.Seq import Seq

record = SeqIO.read(r"C:\Users\zackd\Coding challenge\Day 4 -\rosalind_orf (2).fasta", "fasta")

dna = record.seq
reverse_dna = dna.reverse_complement()

# Transcribe to RNA
forward_rna = dna.transcribe()
reverse_rna = reverse_dna.transcribe()
print(dna)

def get_proteins(rna):
    proteins = set()
    for frame in range(3):
        protein = rna[frame:].translate(to_stop=False)
        aa_seq = str(protein)
        starts = [i for i in range(len(aa_seq)) if aa_seq[i] == 'M']
        for start in starts:
            sub = aa_seq[start:]
            stop = sub.find("*")
            if stop != -1:
                proteins.add(sub[:stop])
    return proteins



# Get proteins from all 6 frames
forward_proteins = get_proteins(forward_rna)
reverse_proteins = get_proteins(reverse_rna)

# Combine all and print unique
all_proteins = forward_proteins.union(reverse_proteins)
print("\n".join(all_proteins))