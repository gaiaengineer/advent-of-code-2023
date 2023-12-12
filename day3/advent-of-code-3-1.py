import re
from typing import Generator, Tuple, List

# Read the content of the CSV file and split it into lines
lines: List[str] = open("C:/Users/Olga Vogel/Desktop/input3.csv").read().splitlines()

def is_symbol(character: str) -> bool:
    # Checks if a character is a symbol.
    return character != "." and not character.isdigit()

def extract_numbers() -> Generator[Tuple[int, str, int, int, int], None, None]:
    # Generates tuples containing the line index, line content, start index, end index, and number for each number in the lines.
    for i, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            # Retrieve the start and end indices of the number and convert it to an integer
            start_index = match.start(0) - 1
            end_index = match.end(0)
            number = int(match.group(0))
            yield i, line, start_index, end_index, number

total_sum = 0

# Iterate over the generated tuples from extract_numbers()
for (
    line_index,
    line_content,
    start_index,
    end_index,
    number,
) in extract_numbers():
    # Check if the number is adjacent to a symbol on either side of the line
    if (start_index >= 0 and is_symbol(line_content[start_index])) or (
        end_index < len(line_content) and is_symbol(line_content[end_index])
    ):
        total_sum += number
        continue

    # Check if the number is adjacent to a symbol above or below in the same column
    for column_index in range(start_index, end_index + 1):
        # Check if we are at the end of the line
        if column_index >= len(line_content):
            continue

        # Check symbols above and below the current line
        if (line_index > 0 and is_symbol(lines[line_index - 1][column_index])) or (
            line_index < len(lines) - 2 and is_symbol(lines[line_index + 1][column_index])
        ):
            total_sum += number
            break

# Print the final total_sum
print(total_sum)