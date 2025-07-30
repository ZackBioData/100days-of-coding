import re
import requests
"""
    this projecct is abandoned, untill further skills are acquired i cannot complete this project yet.
this projecct is abandoned, untill further skills are acquired i cannot complete this project yet.
this projecct is abandoned, untill further skills are acquired i cannot complete this project yet.
this projecct is abandoned, untill further skills are acquired i cannot complete this project yet.
this projecct is abandoned, untill further skills are acquired i cannot complete this project yet.
this projecct is abandoned, untill further skills are acquired i cannot complete this project yet.
this projecct is abandoned, untill further skills are acquired i cannot complete this project yet.
this projecct is abandoned, untill further skills are acquired i cannot complete this project yet.
this projecct is abandoned, untill further skills are acquired i cannot complete this project yet.

    """
# Compile the PROSITE motif using a look‑ahead so we catch overlaps
# (?=(…)) is zero‑width, so the regex engine checks at every position without skipping
motif = re.compile(r"(?=(N[^P][ST][^P]))")

def fetch_sequence(accession: str) -> str:
    """
    Given a UniProt accession (optionally with "_NAME" suffix),
    fetch its protein FASTA from UniProt and return the concatenated sequence.
    """
    # Strip off anything after the first underscore
    acc = accession.split("_", 1)[0]
    url = f"https://www.uniprot.org/uniprot/{acc}.fasta"
    resp = requests.get(url)
    resp.raise_for_status()
    lines = resp.text.splitlines()
    # Skip the header (first line) and join the rest into one sequence string
    return "".join(lines[1:])

def find_motif_positions(seq: str) -> list[str]:
    """
    Scan `seq` for the N‑glycosylation motif N{P}[ST]{P},
    returning all 1‑based start positions (including overlaps).
    """
    # m.start() is 0‑based, so add 1 for Rosalind’s 1‑based indexing
    return [str(m.start() + 1) for m in motif.finditer(seq)]

def main():
    # Read your list of raw UniProt IDs (one per line) from ids_mprt.txt
    with open("ids_mprt.txt") as f:
        raw_ids = [line.strip() for line in f if line.strip()]

    for raw in raw_ids:
        seq = fetch_sequence(raw)
        positions = find_motif_positions(seq)
        if positions:
            # Print the original raw ID, then the space‑separated positions
            print(raw)
            print(" ".join(positions))

if __name__ == "__main__":
    main()
