# _*_ encoding = utf-8 _*_

def reverse_complement(sequence):    
  # Define a dictionary to store the complement of each nucleotide    
  complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}    

# Reverse the input sequence    
reverse_seq = sequence[::-1]  # Reverse the sequence    

# Generate the reverse complement sequence by mapping each base to its complement    
reverse_complement_seq = ''.join(complement[base] for base in reverse_seq)    

# Return the reverse complement sequence    
return reverse_complement_seq

# Example usage:
sequence = 'ATCGATCGATCG'
reverse_comp = reverse_complement(sequence)
print(f'Original Sequence:  {sequence}')
print(f'Reverse Complement: {reverse_comp}'
