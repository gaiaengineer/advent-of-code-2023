# Read the input data from the specified CSV file
with open("C:/Users/Olga Vogel/Desktop/input10.csv", "r") as file:
    lines = file.readlines()

# Define a dictionary to represent the types of pipes and their corresponding reachable directions
pipe_types = {
    "|": ["n", "s"],
    "-": ["w", "e"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
    'S': ["n", "s", "w", "e"],
}

# Define a dictionary to represent directions and their corresponding changes in coordinates
directions = {
    "n": (-1, 0, "s"),
    "s": (1, 0, "n"),
    "w": (0, -1, "e"),
    "e": (0, 1, "w"),
}

# Create a map by converting each line into a list of characters
map = [[c for c in line.strip()] for line in lines]

# Find the starting position marked as 'S' in the map
for i in range(len(map)):
    for j in range(len(map[i])):
        place = map[i][j]
        if place == 'S':
            start = (i, j)

# Initialize a dictionary to store encountered places and their distances from the starting position
encountered_places = dict()

# Initialize a search queue with the starting position and distance 0
search_queue = [(start, 0)]

# Perform a breadth-first search to find the distances to all reachable places
while len(search_queue) > 0:
    current, distance = search_queue.pop(0)
    if current in encountered_places:
        continue
    encountered_places[current] = distance
    i, j = current
    available_directions = pipe_types[map[i][j]]
    for direction in available_directions:
        di, dj, opposite = directions[direction]
        new = (i + di, j + dj)
        if i + di < 0 or i + di >= len(map):
            continue
        if j + dj < 0 or j + dj >= len(map[i + di]):
            continue
        target = map[i + di][j + dj]
        if target not in pipe_types:
            continue
        target_directions = pipe_types[target]
        if opposite in target_directions:
            search_queue.append((new, distance + 1))

# Find the maximum distance from the starting position to any encountered place
max_distance = max(encountered_places.values())

# Print the maximum distance
print(max_distance)

# Define a function to get the type of a pipe based on its reachable directions
def get_pipe_type(i, j):
    reachable_directions = []
    for direction in directions:
        di, dj, opposite = directions[direction]
        if i + di < 0 or i + di >= len(map):
            continue
        if j + dj < 0 or j + dj >= len(map[i + di]):
            continue
        if (i + di, j + dj) not in encountered_places:
            continue
        target = map[i + di][j + dj]
        if target not in pipe_types:
            continue
        target_directions = pipe_types[target]
        if opposite not in target_directions:
            continue
        reachable_directions.append(direction)
    for piece_type in pipe_types:
        if len(reachable_directions) == len(pipe_types[piece_type]):
            if all([direction in pipe_types[piece_type] for direction in reachable_directions]):
                return piece_type
    return None

# Update the type of the starting pipe based on its reachable directions
map[start[0]][start[1]] = get_pipe_type(start[0], start[1])

# Initialize a counter for the number of norths
norths = 0

# Update the map to mark pipes as 'O' or 'I' based on the number of encountered norths
for i in range(len(map)):
    for j in range(len(map[i])):
        place = map[i][j]
        if (i,j) in encountered_places:
            pipe_directions = pipe_types[place]
            if "n" in pipe_directions:
                norths += 1
            continue
        if norths % 2 == 0:
            map[i][j] = "O"
        else:
            map[i][j] = "I"

# Count the number of 'I's in the updated map
inside_count = "\n".join(["".join(line) for line in map]).count("I")
# Print the count of 'I's
print(inside_count)