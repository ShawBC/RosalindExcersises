# Initial Attempt

# with open ('rosalind_rna.txt', 'r') as f:
#     DNA_input = f.read().strip()
#     DNA = list(DNA_input)
#     # replacing all occurrences of 'T' in t with 'U' in u.
#     for i in range (0, len(DNA)):
#         if DNA[i] == 'T':
#             DNA[i] = 'U'
#     RNA = DNA


# Neater Solution using python str replace
with open ('rosalind_rna.txt', 'r') as f:
    dna = f.read().strip()
    rna = dna.replace('T', 'U')
    
    print(rna)