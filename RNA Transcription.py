def to_rna(dna_strand):
    nt=''
    for char in dna_strand:
        if char=='G':
            nt+='C'
        elif char=='C':
            nt+='G'
        elif char=='T':
            nt+='A'
        elif char=='A':
            nt+='U'
        else:
            nt+=char
    return nt
