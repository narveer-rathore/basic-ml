from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.externals.six import StringIO

import pydotplus
import numpy as np

data = load_iris()

# first entry for setosa, versicolor and virginica
test_indexes = [0, 50, 100]

# training data
train_target = np.delete(data.target, test_indexes)
train_data = np.delete(data.data, test_indexes, axis=0)

# test data
test_target = data.target[test_indexes]
test_data = data.data[test_indexes]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_target)

print([test_target])
print(clf.predict(test_data))


dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")
