import re
from typing import List, Tuple

# Read the content of the CSV file and split it into lines
lines: List[str] = open("C:/Users/Olga Vogel/Desktop/input3.csv").read().splitlines()

def is_not_dot_or_digit(char: str) -> bool:
    # Checks if a character is not a dot or a digit.
    return char != "." and not char.isdigit()

def extract_parts() -> List[List[Tuple[int, int, int]]]:
    # Extracts the parts from the lines.
    # Returns a list of parts for each line.
    parts: List[List[Tuple[int, int, int]]] = []
    for i, line in enumerate(lines):
        parts.append([])

        for match in re.finditer(r"\d+", line):
            # Retrieve start index, end index, and number for each part
            start_index = match.start(0) - 1
            end_index = match.end(0)
            number = int(match.group(0))
            part = (start_index, end_index, number)
            parts[i].append(part)

    return parts

total_product = 0
parts_list: List[List[Tuple[int, int, int]]] = extract_parts()

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != "*":
            continue

        adjacent_parts: List[int] = []

        for k in range(-1, 2):
            if i + k < 0 or i + k >= len(lines):
                continue

            for start_index, end_index, number in parts_list[i + k]:
                if start_index <= j <= end_index:
                    adjacent_parts.append(number)

        if len(adjacent_parts) == 2:
            total_product += adjacent_parts[0] * adjacent_parts[1]

# Print the final total_product
print(total_product)