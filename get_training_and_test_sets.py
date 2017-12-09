from calculate_row_length import calculate_row_length, get_row_height
from calculate_mean_distance import calculate_mean_distance
from calculate_distance_to_neighbours import calculate_distance_to_neighbours
from get_label_for_row import get_label_for_row, get_row_boundaries
from sort_row_by_x import sort_row_by_x
from has_bold_word import has_bold_word
import numpy as np



def get_data_set(pdfs, tables_boundaries):
    labels = []
    dataset = []
    for pdf in pdfs:
        for page in pdf:
            for row in page:
                if len(row) >= 1 and len(row[0].keys()) != 0:
                    row = sort_row_by_x(row)
                    rowIndex = page.index(row)
                    if rowIndex == 0:
                        upper = row
                    else:
                        upper = page[rowIndex - 1]

                    if rowIndex == len(page) - 1 or len(page[rowIndex + 1][0].keys()) == 0:
                        lower = row
                    else:
                        lower = page[rowIndex + 1]
                    features = get_feature_set(upper, row, lower)
                    features.append(pdfs.index(pdf))
                    features.append(pdf.index(page))
                    dataset.append(features)
                    
                    labels.append(get_label_for_row(row, tables_boundaries[pdfs.index(pdf)]))

    return [dataset, labels]

def get_feature_set(upper, row, lower):
    feature_set = []
    feature_set.append(calculate_row_length(row))
    #nr cuvintelor de pe o linie
    feature_set.append(len(row))
    feature_set.append(get_row_height(row))
    feature_set.append(calculate_mean_distance(row))
    feature_set.append(has_bold_word(row))
    distance_to_neighbours = calculate_distance_to_neighbours(upper, row, lower)
    feature_set.append(distance_to_neighbours[0])
    feature_set.append(distance_to_neighbours[1])
    row_boundaries = get_row_boundaries(row)
    feature_set = feature_set + row_boundaries
    return feature_set
