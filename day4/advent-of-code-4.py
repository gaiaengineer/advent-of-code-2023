import re

# Define a class to represent a single scratchcard
class Scratchcard:
    def __init__(self, card: str):
        # Split the input string to extract card information
        card_id, winning_numbers, numbers_i_have = re.split(r"[:|]", card)

        # Extract and set card properties
        self.id = int(card_id.split()[1])
        self.winning_numbers = set(
            int(winning_number) for winning_number in winning_numbers.split()
        )
        self.numbers_i_have = set(
            int(numbers_i_have) for numbers_i_have in numbers_i_have.split()
        )
        self.winning_numbers_i_have = self.winning_numbers.intersection(
            self.numbers_i_have
        )

    # Calculate and return the points based on the scratchcard's winning numbers
    def get_points(self) -> int:
        if not self.winning_numbers_i_have:
            return 0

        return 2 ** (len(self.winning_numbers_i_have) - 1)

    # Get a tuple of copy IDs based on the scratchcard's winning numbers
    def get_copies_id(self) -> tuple[int, ...]:
        return tuple(
            self.id + index + 1 for index, _ in enumerate(self.winning_numbers_i_have)
        )

# Define a class to represent a pile of scratchcards
class Pile:
    def __init__(self, multi_lines_str: str):
        # Create a list of Scratchcard objects from the input string
        self.cards = [Scratchcard(line) for line in multi_lines_str.splitlines()]

    # Calculate and return the total points of the pile of scratchcards
    def get_total_points(self) -> int:
        total_points = 0

        # Iterate through each scratchcard and accumulate points
        for card in self.cards:
            total_points += card.get_points()

        return total_points

    # Calculate and return the number of copies for each scratchcard in a dictionary
    def get_number_of_copies(self) -> dict[int, int]:
        number_of_copies = {card.id: 1 for card in self.cards}

        # Iterate through each scratchcard and update the number of copies dictionary
        for card in self.cards:
            for _ in range(number_of_copies[card.id]):
                for copy_id in card.get_copies_id():
                    number_of_copies[copy_id] += 1

        return number_of_copies

if __name__ == "__main__":
    # Read input from a file and calculate and print the total points and number of copies
    with open("C:/Users/Olga Vogel/Desktop/input4.csv", "r") as file:
        input_text = file.read()
        print(Pile(input_text).get_total_points())
        print(sum(Pile(input_text).get_number_of_copies().values()))