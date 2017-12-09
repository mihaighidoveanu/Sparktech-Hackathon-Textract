def get_label_for_row(row, pdf):
    boundaries = get_row_boundaries(row)
    for pages in pdf:
        for table in pages:
            if is_in_table(boundaries, table) == True:
                return 1
    else:
        return 0



def get_row_boundaries(row):
    x1 = row[0]['x']
    y1 = row[0]['y']

    x2 = row[len(row) - 1]['x'] + row[len(row) - 1]['w']
    y2 = row[len(row) - 1]['y'] + row[len(row) - 1]['h']

    return [x1, y1, x2, y2]

def is_in_table(boundaries, table_boundaries):
    if boundaries[0] >= table_boundaries[0]:
        if boundaries[1] >= table_boundaries[1]:
            if boundaries[2] <= table_boundaries[2]:
                if boundaries[3] <= table_boundaries[3]:
                    return True
    return False
