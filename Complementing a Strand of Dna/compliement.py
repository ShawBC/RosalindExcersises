with open('rosalind_revc.txt', 'r') as f:
    dna = f.read().strip()

    reversed_dna = list(dna[::-1])


    for i in range(0, len(reversed_dna)):
        if reversed_dna[i] == 'A':
            reversed_dna[i] = 'T'
        elif reversed_dna[i] == 'T':
            reversed_dna[i] = 'A'
        elif reversed_dna[i] == 'C':
            reversed_dna[i] = 'G'
        elif reversed_dna[i] == 'G':
            reversed_dna[i] = 'C'

print(f"".join(reversed_dna))