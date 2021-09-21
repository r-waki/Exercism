def to_rna(dna_strand):
    table = str.maketrans("CGTA", "GCAU")
    return dna_strand.translate(table)
