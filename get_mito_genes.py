# _*_ encoding = utf-8 _*_
# Open .fa file and read its contents
input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'mito_genes.fa'

sequences = {}

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
f.write(f'>{name} {sequence}\n')
print(f'Original sequences saved to {output_file}')
