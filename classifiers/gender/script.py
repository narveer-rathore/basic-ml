from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

classifiers = [
	DecisionTreeClassifier(),
	KNeighborsClassifier(),
	RandomForestClassifier(),
	MLPClassifier()
]

# Samples [height, weight, shoe size]
data = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
	[166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40],
	[159, 55, 37], [171, 75, 42], [181, 85, 43]]


label = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

for clf in classifiers:
	clf = clf.fit(data, label)

h = int(input('Height : '))
w = int(input('Weight : '))
s = int(input('Shoe Size : '))

print("Results")
for clf in classifiers:
	prediction = clf.predict([[h, w, s]])
	accuracy = accuracy_score(label, clf.predict(data)) * 100
	print("{} predicted {} with {} accuracy.".format(clf.__class__.__name__, prediction, accuracy.round(2)))
