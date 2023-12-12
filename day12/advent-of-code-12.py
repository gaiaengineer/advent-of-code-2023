# Importing the functools module for the cache decorator, which helps memoize function calls
from functools import cache

# Importing data from the specified CSV file
with open("C:/Users/Olga Vogel/Desktop/input12.csv") as file:
    # Splitting each line into a list of words and storing them in the word_sets variable
    word_sets = [line.split() for line in file.read().strip().split("\n")]

# Define a function calculate_solutions with memoization using the cache decorator
@cache
def calculate_solutions(pattern, sizes, group_size_count=0):
    # Base case: if the pattern is empty, check if sizes and group_size_count are also empty
    if not pattern:
        return not sizes and not group_size_count
    
    # Initialize the number of solutions
    total_solutions = 0
    
    # Determine the possible values for the current character in the pattern
    possible_chars = [".", "#"] if pattern[0] == "?" else pattern[0]
    
    # Iterate through the possibilities
    for char in possible_chars:
        if char == "#":
            # Recursively call calculate_solutions with updated parameters
            total_solutions += calculate_solutions(pattern[1:], sizes, group_size_count + 1)
        else:
            if group_size_count:
                # Check if there are sizes remaining and the current group size matches group_size_count
                if sizes and sizes[0] == group_size_count:
                    # Recursively call calculate_solutions with updated parameters
                    total_solutions += calculate_solutions(pattern[1:], sizes[1:])
            else:
                # Recursively call calculate_solutions with updated parameters
                total_solutions += calculate_solutions(pattern[1:], sizes)
    
    # Return the total number of solutions
    return total_solutions

# Create a list of tuples, where each tuple contains a group string and a tuple of sizes
group_info_list = [(group, tuple(map(int, sizes_str.split(",")))) for group, sizes_str in word_sets]

# Print the sum of solutions for each row, considering the original and extended groupings
print(sum(calculate_solutions(group_pattern + ".", sizes) for group_pattern, sizes in group_info_list))
print(sum(calculate_solutions("?".join([group_pattern] * 5) + ".", sizes * 5) for group_pattern, sizes in group_info_list))
