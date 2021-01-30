from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

features = iris.data
labels = iris.target

clf = KNeighborsClassifier()
clf.fit(features, labels)

SepalLength = int(input('Enter Sepal Length in cm\n'))
SepalWidth = int(input('Enter Sepal Width in cm\n'))
PetalLength = int(input('Enter Petal Length in cm\n'))
PetalWidth = int(input('Enter Petal Length in cm\n'))

preds = clf.predict([[SepalLength, SepalWidth, PetalLength, PetalWidth]])

# print(iris.DESCR)
# print(preds)
# print(features[0], labels[0])

Info = 'The plant is'

if preds == 0:
    print(Info, 'Iris-Setosa')
elif preds == 1:
    print(Info, 'Iris-Versicolour')
else:
    print(Info, 'Iris-Virginica')





