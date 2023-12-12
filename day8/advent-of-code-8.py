# Import the greatest common divisor (gcd) function from the math library
from math import gcd
# Import the reduce function from the functools library
from functools import reduce

# Define a function to follow the given instructions in the network
def follow_instructions(instructions, current_node):
    # Iterate through each instruction and update the current node accordingly
    for instruction in instructions:
        if instruction == "L":
            current_node = network[current_node][0]
        elif instruction == "R":
            current_node = network[current_node][1]
    return current_node

# Read input data from the specified CSV file
with open("C:/Users/Olga Vogel/Desktop/input8.csv", "r") as file:
    input_data = file.read().splitlines()

# Extract instructions and initialize variables
instructions = input_data[0]
inst_len = len(instructions)
network = {}
steps = 0

# Build the network based on the input data
for line in input_data[2:]:
    node, connections = line.split(" = ")
    connections = connections[1:-1].split(", ")
    network[node] = connections

# Initialize the current node for the first part of the task
current_node = "AAA"

# Follow instructions until reaching the node "ZZZ" and count the steps
while current_node != "ZZZ":
    current_node = follow_instructions(instructions, current_node)
    steps += inst_len

# Print the solution for the first part of the task
print("Solution 1: ", steps)

# Find all nodes ending with "A" as starting nodes for the second part
current_nodes = [node for node in network if node[-1] == "A"]
steps_needed = []
steps = 0

# Iterate until there are no more current nodes
while len(current_nodes) > 0:
    new_current_nodes = []
    steps += inst_len
    # Follow instructions for each current node and update the list of current nodes
    for current_node in current_nodes:
        new_node = follow_instructions(instructions, current_node)

        # Check if the new node ends with "Z" and update the steps needed
        if new_node[-1] == "Z":
            steps_needed.append(steps)
        else:
            new_current_nodes.append(new_node)

    current_nodes = new_current_nodes

# Define a function to calculate the least common multiple (LCM) of two numbers
def lcm(a, b):
    return a * b // gcd(a, b)

# Calculate the solution for the second part using the LCM of the steps needed
solution2 = reduce(lcm, steps_needed)
# Print the solution for the second part of the task
print("Solution 2: ", solution2)
