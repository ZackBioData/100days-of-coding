output_path = "mastoparan_variants.txt"
out = open(output_path, "w")

genes_of_interest = ["LDLR", "BCL2", "PCP4", "VDAC1", "ATP2B1"]

with open(r"C:\Users\zackd\Bioinformatics\clinvar.vcf", "r") as f:

    for line in f:
        if line.startswith("#"):
            continue  # skip header lines

        cols = line.strip().split("\t")
        chrom = cols[0].replace("chr", "")
        pos = int(cols[1])
        ref = cols[3]
        alt = cols[4]
        info = cols[7]

        # Parse INFO into dictionary
        info_dict = dict(item.split('=') for item in info.split(';') if '=' in item)
        gene_info = info_dict.get("GENEINFO", "")

        # See if any gene in the list appears in the GENEINFO field
        for gene in genes_of_interest:
            if gene in gene_info:
                significance = info_dict.get("CLNSIG", "NA")
                disease = info_dict.get("CLNDN", "NA")
                review = info_dict.get("CLNREVSTAT", "NA")

                # Output
                out.write(f"{chrom}:{pos} {ref}>{alt}\n")
                out.write(f"   Gene: {gene}\n")
                out.write(f"   Significance: {significance}\n")
                out.write(f"   Disease: {disease}\n")
                out.write(f"   Review: {review}\n\n")
                break  # Avoid writing the same variant twice if multiple gene names match

out.close()
