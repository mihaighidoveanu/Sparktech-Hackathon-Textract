def calculate_distance_to_neighbours(upper_neighbour, row, lower_neighbour):
    return [row[0]['y'] - (upper_neighbour[0]['y'] + upper_neighbour[0]['h']), lower_neighbour[0]['y'] - (row[0]['y'] + row[0]['h'])]
