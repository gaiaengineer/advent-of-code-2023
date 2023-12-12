from collections import Counter

# Read data from the specified CSV file and store it in the 'data' variable
with open("C:/Users/Olga Vogel/Desktop/input7.csv") as f:
    data = f.read().strip()

# Define a function to determine the type of a poker hand
def hand_type(hand):
    # Count the occurrences of each card in the hand
    c = Counter(hand)
    # Handle jokers in the hand by extracting their count and adjusting the counts list
    counts = [0] if (jokers := c.pop("*", 0)) == 5 else sorted(c.values())
    counts[-1] += jokers

    # Match the counts list to determine the poker hand type
    match counts:
        case *_, 5:
            return 7
        case *_, 4:
            return 6
        case *_, 2, 3:
            return 5
        case *_, 3:
            return 4
        case *_, 2, 2:
            return 3
        case *_, 2:
            return 2
    return 1

# Define a function to solve the poker game based on the input data
def solve(data):
    # Split each line into a list of cards and bids
    ws = [l.split() for l in data.split("\n")]
    # Calculate the total score by sorting and enumerating hand types and multiplying by bids
    return sum(
        rank * bid
        for rank, (*_, bid) in enumerate(
            sorted(
                (hand_type(hand), *map("*23456789TJQKA".index, hand), int(bid))
                for hand, bid in ws
            ),
            1,
        )
    )

# Print the results for both the original data and the data with 'J' replaced by '*'
print(solve(data))
print(solve(data.replace("J", "*")))
