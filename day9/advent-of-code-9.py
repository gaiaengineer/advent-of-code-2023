# Read and parse the input data from the specified CSV file into a list of lists
input_data = [[int(i) for i in s.split()] for s in open('C:/Users/Olga Vogel/Desktop/input9.csv').read().split('\n') if s.strip()]

# Define a recursive function 'calculate_result' and an alternative list name 'differences'
def calculate_result(sequence):
    # Check if the sum of non-zero elements in the sequence is zero
    if sum(i != 0 for i in sequence) == 0:
        return 0
    
    # Initialize an empty list 'differences' to store the differences between consecutive elements
    differences = []
    for i in range(len(sequence)-1):
        differences.append(sequence[i+1] - sequence[i])
    
    # Recursively calculate the result using the modified sequence 'differences'
    return sequence[-1] + calculate_result(differences)

# Print the sum of 'calculate_result' for each sequence in the input data and its reversed version
print(sum(calculate_result(sequence) for sequence in input_data))
print(sum(calculate_result(sequence[::-1]) for sequence in input_data))