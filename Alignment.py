# _*_ encoding = utf-8 _*_
def read_blosum62(file_path): 
  """    
Read the BLOSUM62 replacement matrix from the given file path.
Args:   
- file_path (str): BLOSUM62 
The path of the matrix file
Returns:    
- dict: A nested dictionary representing the replacement matrix of BLOSUM62. The first layer of bonds is amino acids, the second layer of bonds is other amino acids, and the value is the substitution fraction between them.    
""" 
with open(file_path, 'r') as f:  
lines = f.readlines() 
#Analyze header information and extract column labels
header = lines[0].strip().split()
# Initialize the dictionary for replacing the BLOSUM62 matrix
matrix = {} 
# Analyze each row and construct a replacement matrix
for line in lines[1:]: 
row = line.strip().split()
amino_acid = row[0]
# Create a replacement score dictionary for the current amino acid
matrix[amino_acid] = {header[i]: int(row[i + 1]) for i in range(len(header))} 
return matrixdef calculate_similarity(seq1, seq2, blosum62):
"""
Calculate the similarity score between two sequences and replace the matrix with the given BLOSUM62.
Args:
- seq1 (str): The first amino acid sequence
- seq2 (str): The second amino acid sequence.
- blosum62 (dict): A nested dictionary representing the replacement matrix of BLOSUM62. The first layer of bonds is amino acids, the second layer of bonds is other amino acids, and the value is the substitution fraction between them.
Returns: 
- float:The calculated similarity score ranges from negative infinity to positive infinity.
Raises:
- ValueError:If the lengths of the two input sequences are not equal. 
Notes: 
-If the amino acids in the sequence do not have corresponding scores in the BLOSUM62 substitution matrix, the default value of -4 is used for punishment.
""" 
#Check if the sequence lengths are equal, if not, throw an exception
if len(seq1) != len(seq2):        
raise ValueError("Sequences must be of the same length")
# Initialize similarity score and count of identical amino acid pairsscore = 0 
identical_pairs = 0 
# Traverse the amino acid pairs at each position of two sequences
for aa1, aa2 in zip(seq1, seq2):        
#Check if there is a defined score for the current amino acid pair in the BLOSUM62 substitution matrix      
if aa1 in blosum62 and aa2 in blosum62[aa1]:            
# If there is a definition, accumulate the corresponding scores
score += blosum62[aa1][aa2] 
# If amino acid pairs are the same, increase the count of identical pairs            
if aa1 == aa2:               
identical_pairs += 1       
else:           
# If not defined, use default penalty value-4            
score -= -4  
# Use default penalty value-4   
# Calculate the percentage of identical amino acid pairs   
percent_identical = (identical_pairs / len(seq1)) * 100    
percent_identical_formatted = f"{percent_identical:.2f}%"   
# Return similarity score, as well as the number and percentage of identical amino acid pairs   
return score , identical_pairs, percent_identical_formatteddef compare_sequences(seq1, seq2, blosum62):    
similarity,identical_pairs, percent_identical = calculate_similarity(seq1, seq2, blosum62)    
return similarity,identical_pairs, percent_identical# 读取BLOSUM62矩阵blosum62 = read_blosum62('blosum62.txt')
#Define sequence
human 
= "MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
random 
="MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
mouse  
="WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL"
# Calculate similarity
print("Human:%s" % human)
print("Mouse:%s" % mouse)
print("Random:%s" % random)
human_vs_random,identical_pairs1,       percent_identical1 
compare_sequences(human, random, blosum62)
human_vs_mouse,identical_pairs2,        percent_identical2
compare_sequences(human, mouse, blosum62)
mouse_vs_random,identical_pairs3,       percent_identical3 
compare_sequences(mouse, random, blosum62)
# Output result
print("Human vs Random:", human_vs_random)
print("identical_pairs:",identical_pairs1)
print("percent_identical",percent_identical1,"\n")
print("Human vs Mouse:", human_vs_mouse)
print("identical_pairs:",identical_pairs2)
print("percent_identical",percent_identical2,"\n")
print("Mouse vs Random:", mouse_vs_random)
print("identical_pairs:",identical_pairs3)
print("percent_identical",percent_identical3,"\n")
# Find the two closest sequences (find the one with the highest score)
max_similarity = max(human_vs_random, human_vs_mouse, mouse_vs_random)
if max_similarity == human_vs_random:    
  print("The most closely related sequences are Human and Random.")
elif max_similarity == human_vs_mouse:    
  print("The most closely related sequences are Human and Mouse.")
else:    
  print("The most closely related sequences are Mouse and Random.")
