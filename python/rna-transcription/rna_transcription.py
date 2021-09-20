def to_rna(dna_strand):
    if dna_strand == "":
        return ""

    dna_strand = list(dna_strand)
    rna_strand = ""
    for dna in dna_strand:
        if dna == "C":
            rna_strand = f"{rna_strand}G"
        elif dna == "G":
            rna_strand = f"{rna_strand}C"
        elif dna == "T":
            rna_strand = f"{rna_strand}A"
        elif dna == "A":
            rna_strand = f"{rna_strand}U"

    return rna_strand
