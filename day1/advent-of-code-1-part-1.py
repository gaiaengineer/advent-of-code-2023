# Import the 'csv' module to work with CSV files
import csv

# Define a function to extract the first and last digit from a string
def extract_first_and_last_digit(s):
    # Find the first digit in the string using a generator expression
    first_digit = next((c for c in s if c.isdigit()), '0')
    # Find the last digit in the reversed string using a generator expression
    last_digit = next((c for c in reversed(s) if c.isdigit()), '0')
    # Return the first and last digits as a tuple
    return first_digit, last_digit

# Define a function to process strings from a CSV file
def process_strings_from_csv(file_path):
    # Initialize an empty list to store strings from the CSV file
    strings_list = []
    # Open the CSV file using the 'csv.reader' and read each row
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Iterate through each row in the CSV file
        for row in reader:
            # Extend the 'strings_list' with the strings from the current row
            strings_list.extend(row)

    # Initialize a variable to store the total sum of two-digit numbers
    total_sum = 0
    # Iterate through each string in the 'strings_list'
    for string in strings_list:
        # Extract the first and last digit from the string
        first_digit, last_digit = extract_first_and_last_digit(string)
        # Concatenate the first and last digits and convert to an integer
        two_digit_number = int(first_digit + last_digit)
        # Add the two-digit number to the total sum
        total_sum += two_digit_number

    # Return the total sum
    return total_sum

# Specify the file path of the CSV file
csv_file_path = 'C:/Users/Olga Vogel/Desktop/input.csv'

# Call the 'process_strings_from_csv' function with the specified file path
result = process_strings_from_csv(csv_file_path)

# Print the result (total sum of two-digit numbers)
print(result)