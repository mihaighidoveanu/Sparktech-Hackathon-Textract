#mean distance between words
def calculate_mean_distance(row):
    distance = 0
    for index in range(0 , len(row) - 1):
        distance += row[index + 1]['x'] - row[index]['x'] + row[index]['w']

    distance /= len(row)
    return distance
