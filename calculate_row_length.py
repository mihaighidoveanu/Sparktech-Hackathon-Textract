def calculate_row_length(row):
    return row[len(row) - 1]['x'] - row[0]['x'] + row[len(row) - 1]['w']


def get_row_height(row):
    return row[0]['h']
