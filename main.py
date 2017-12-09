import numpy as np
import glob
from sklearn.svm import SVC

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

X_train = X[0:len(X) / 2]
X_test = X[len(X) / 2 + 1:len(X) - 1]

y_train = y[0:len(y) / 2]
y_test = y[len(y) / 2 + 1:len(y) - 1]


clf = SVC()
clf.fit(X_train, y_train)
print clf.score(X_test, y_test)
