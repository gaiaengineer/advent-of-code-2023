# Read the input data from the specified CSV file and strip each entry
lines = []
with open('C:/Users/Olga Vogel/Desktop/input11.csv') as file:
    raw_lines = file.readlines()
    lines = [entry.strip() for entry in raw_lines]

def relocate_galaxies(galaxies, axis, sky_map, value_to_expand, old_galaxies):
    # Adjust the value to expand
    value_to_expand = value_to_expand - 1 if value_to_expand != 1 else value_to_expand
    add_value = 0
    length_to_check = len(sky_map) if axis == 0 else len(sky_map[0])

    # Iterate through the map to relocate galaxies
    for i in range(1, length_to_check - 1):
        # Check if there are no galaxies at the current position
        if all(galaxy[axis] != i for galaxy in old_galaxies):
            # Find galaxies to relocate
            galaxies_to_relocate = [galaxy for galaxy in galaxies if galaxy[axis] > i + add_value]

            for galaxy in galaxies_to_relocate:
                galaxies.remove(galaxy)

                # Expand in the Y-axis if axis is 0, or expand in the X-axis if axis is 1
                expand_in_y_axis = value_to_expand if axis == 0 else 0
                expand_in_x_axis = value_to_expand if axis == 1 else 0
                galaxies.append((galaxy[0] + expand_in_y_axis, galaxy[1] + expand_in_x_axis))

            add_value += value_to_expand

    return galaxies

def task_result(lines, value_to_expand):
    import re

    old_galaxies = []
    sky_map = []

    # Parse the input lines to find galaxies and build the sky map
    for i, line in enumerate(lines):
        sky_map.append(list(line))

        found_galaxies = re.finditer(r'#', line)
        [old_galaxies.append((i, galaxy.start())) for galaxy in found_galaxies]

    galaxies = old_galaxies.copy()

    # Relocate galaxies in the Y-axis and then in the X-axis
    galaxies = relocate_galaxies(galaxies, 0, sky_map, value_to_expand, old_galaxies)
    galaxies = relocate_galaxies(galaxies, 1, sky_map, value_to_expand, old_galaxies)

    distance = 0

    # Calculate the Manhattan distance between each pair of galaxies
    for i, g1 in enumerate(galaxies):
        for g2 in galaxies[i + 1:]:
            # Manhattan distance formula: |x1 - x2| + |y1 - y2|
            distance += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

    return distance

# Print the task result for the given value to expand (1 and 1000000)
print(task_result(lines, 1))
print(task_result(lines, 1000000))
