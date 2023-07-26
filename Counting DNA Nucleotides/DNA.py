with open ('rosalind_dna.txt', 'r') as f:
    dna = f.read().strip()
    nucleobases = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for base in dna:
        nucleobases[base] += 1
    print(nucleobases)