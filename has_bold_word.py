def has_bold_word(row):
    for word in row:
        if word['bold'] == 1:
            return True
    else:
        return False
