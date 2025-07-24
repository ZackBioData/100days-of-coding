from Bio import SeqIO
from Bio.Seq import Seq

# Load FASTA file
records = list(SeqIO.parse("rosalind_splc.fasta", "fasta"))

# First record is the DNA with introns
full_dna = str(records[0].seq)

# Remaining records are introns
introns = [str(rec.seq) for rec in records[1:]]

# Remove all introns from the full sequence
for intron in introns:
    full_dna = full_dna.replace(intron, "")

# Transcribe and translate
rna = Seq(full_dna).transcribe()
protein = rna.translate(to_stop=True)

print(protein)
