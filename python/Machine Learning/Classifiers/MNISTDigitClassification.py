from sklearn.datasets import fetch_openml
import matplotlib
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split

from sklearn import datasets

digits = datasets.load_digits()

images = digits.images
labels = digits.target

classifier = svm.SVC(gamma=0.001)
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.33, random_state=42)

fit = classifier.fit(X_train, y_train)

plt.gray()
test_img = X_test[1].reshape(8, 8)
imgplot = plt.imshow(test_img)
print("label: ", y_test[1])


t = X_test[1].reshape(1, -1)
pred = classifier.predict(t)
print("prediction: ", pred)
plt.show()


