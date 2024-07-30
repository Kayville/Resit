# _*_ encoding = utf-8 _*_
input_file = input("Please input the original file:")
output_file = input("Please input the output file:")
sequences = {}
def reverse_complement(sequence):    
  # Define a dictionary to store the complement of each nucleotide    
  complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}    

  # Reverse the input sequence    
  reverse_seq = sequence[::-1]  # Reverse the sequence    

  # Generate the reverse complement sequence by mapping each base to its complement    
  reverse_complement_seq = ''.join(complement[base] for base in reverse_seq)    

  # Return the reverse complement sequence    
  return reverse_complement_seq
  with open(input_file, 'r') as f:    
    current_sequence_name = ''    
    current_sequence = []    

    # Iterate through the file content to extract sequences    
    for line in f:        
      line = line.strip()        
      if line.startswith('>'):            
      if current_sequence_name != '':               
        sequences[current_sequence_name] = ''.join(current_sequence)                
        current_sequence = []           
        current_sequence_name = line.split()[0].replace(">", "")       
      else:           
        current_sequence.append(line)    
# Process the last sequence    
        if current_sequence_name != '':        
          sequences[current_sequence_name] = ''.join(current_sequence)

          
# Write to a new .fa file
          with open(output_file, 'w') as f:    
          for name, sequence in sequences.items():        
            reverse_complement_seq = reverse_complement(sequence)
                   f.write(f'>{name} {sequence}\n')
            print(f'Original sequences saved to {output_file}')
