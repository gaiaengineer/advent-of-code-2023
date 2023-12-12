import re
from math import prod

# Read data from the specified CSV file and store it in the 'data' variable
with open("C:/Users/Olga Vogel/Desktop/input6.csv", "r") as file:
    data = file.read().strip()

# Extract race information from the data and organize it in the 'races' list
races = list(zip(*(map(int, re.findall(r"(\d+)", x)) for x in data.split("\n"))))

# Define a binary search function to find a threshold value for a given time and distance
def binary_search(time, dist, left=True):
    lo, hi = 0, time
    while lo <= hi:
        mid = lo + (hi - lo >> 1)
        # Adjust the threshold based on whether it's for the left or right boundary
        if mid * (time - mid) > dist:
            if left:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if left:
                lo = mid + 1
            else:
                hi = mid - 1
    return lo if left else hi

# Define a function to calculate the number of winners for a given time and distance
def num_winners(time, dist):
    return binary_search(time, dist, False) - binary_search(time, dist) + 1

# Define a function for part one of the task
def part_one():
    # Calculate the product of the number of winners for each race
    return prod(num_winners(t, d) for t, d in races)

# Define a function for part two of the task
def part_two():
    # Convert each digit in the zipped races to a single integer and calculate the number of winners
    return num_winners(*(int("".join(str(x) for x in race)) for race in zip(*races)))

# Print the results for both parts of the task
print(f"Part 1: {part_one()}")  
print(f"Part 2: {part_two()}")  
