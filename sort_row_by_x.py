def sort_row_by_x(row):
    row.sort(key=lambda word: word["x"])
    return row
