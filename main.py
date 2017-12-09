import numpy as np
import glob
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

from get_training_and_test_sets import get_data_set
from read_pdf_from_json import read_pdf_from_json
from extractXML import extractXML

xml_paths = glob.glob('../Textract2017/GroundTruth/*');
json_paths = glob.glob('../Textract2017/JSON/*')

pdfs = []
for path in json_paths:
    pdfs.append(read_pdf_from_json(path))


tables_boundaries = []
for path in xml_paths:
    if path.find('-reg') != -1:
        tables_boundaries.append(extractXML(path))


[X, y] = get_data_set(pdfs, tables_boundaries)

# X_train = X[0:len(X) / 2]
# X_test = X[len(X) / 2 + 1:len(X) - 1]
#
# y_train = y[0:len(y) / 2]
# y_test = y[len(y) / 2 + 1:len(y) - 1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = SVC()
clf.fit(X_train, y_train)
print clf.score(X_test, y_test)

predict = clf.predict(X_train)


for index in range(0, len(X_test)):
    features = X_test[index]
    row_boundaries = features[len(features) - 6 : len(features) - 2]
    pdf_number = features[len(features) - 2]
    pdf_page = features[len(features) - 1]

    if predict[index] == 1:
        neighbour_pdf_number = 0
        neighbour_pdf_page = 0
        neighbour_boundaries = []
        nr_lines = 0
        index += 1
        while predict[index] == 1:
            neighbour = X_test[index]
            neighbour_pdf_number = neighbour[len(neighbour) - 2]
            neighbour_pdf_page = neighbour[len(neighbour) - 1]
            neighbour_boundaries = neighbour[len(neighbour) - 6 : len(neighbour) - 2]
            index += 1
            nr_lines += 1
        if nr_lines > 0:
            print row_boundaries[:2], neighbour_boundaries[2:4]
        index -= 1
