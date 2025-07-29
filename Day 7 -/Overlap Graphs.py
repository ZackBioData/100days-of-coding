from Bio import SeqIO

k = 3
records = list(SeqIO.parse("rosalind_grph (1).fasta", "fasta"))

for record in records:
    record_suffix = str(record.seq)[-k:]
    for other_record in records:
        if record.id == other_record.id:
            continue
        other_prefix = str(other_record.seq)[:k]
        if record_suffix == other_prefix:
            print(record.id, other_record.id)
