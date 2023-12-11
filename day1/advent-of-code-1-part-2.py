import csv
import re
# Install the 'word2number' module
from word2number import w2n  

# Open the CSV file and extract the document:
with open('C:/Users/Olga Vogel/Desktop/input.csv', mode='r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    strings = list(reader)

# The final number (a sum of all two-digit numbers)
result: int = 0

# Iterate over every single line of the calibration document:
for line in strings:

    # Search for a number, either as digits or as a spelled-out number
    matches = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", ','.join(line))

    # Convert all the spelled-out numbers into digits
    matches = [w2n.word_to_num(match) if not match.isdigit() else match for match in matches]

    # Concatenate the first and last digit from every line
    first_last = f"{matches[0]}{matches[-1]}"

    # Convert them into an int and add them up to the result
    result += int(first_last)

    # Here's a nice way to see the results and check if everything is all right
    print(f"String: {line}, Resulting Two-digit Number: {first_last}") 

print(result)