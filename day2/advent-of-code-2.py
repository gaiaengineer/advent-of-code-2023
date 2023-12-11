import math
import re

# defaultdict is a class in the collections module of Python that inherits from the built-in dict class. 
# It overrides one method to provide a default value for a nonexistent key, specified when you create the defaultdict. 
# This can be particularly useful when working with dictionaries, as it eliminates the need to check whether a key exists before updating or accessing its value.

from collections import defaultdict

# Read the contents of the CSV file into a list of strings
with open("C:/Users/Olga Vogel/Desktop/input2.csv") as x:
    ls = x.read().strip().split("\n")

# Initialize variables for counting possible IDs and summing power
possible_ids = 0
sum_power = 0

# Iterate through each line in the input file
for l in ls:
    # Remove special characters (;,:), split the line into parts
    parts = re.sub("[;,:]", "", l).split()

    # Create a defaultdict to store the maximum count for each color
    colormax = defaultdict(int)

    # Iterate through pairs of count and color in the parts
    for count, color in zip(parts[2::2], parts[3::2]):
        # Update the maximum count for each color
        colormax[color] = max(colormax[color], int(count))

    # Check if the conditions for red, green, and blue colors are met
    if colormax["red"] <= 12 and colormax["green"] <= 13 and colormax["blue"] <= 14:
        # If conditions are met, add the ID to the possible_ids count
        possible_ids += int(parts[1])

    # Calculate the product of all maximum color counts and add it to sum_power
    sum_power += math.prod(colormax.values())

# Print the result for Part 1
print("Part 1:", possible_ids)

# Print the result for Part 2
print("Part 2:", sum_power)