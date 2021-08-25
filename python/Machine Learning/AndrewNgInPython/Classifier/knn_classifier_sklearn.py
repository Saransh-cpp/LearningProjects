from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

data = datasets.load_iris()

classifier = KNeighborsClassifier()
classifier.fit(data['data'][:-30], data['target'][:-30])

predicted_category = classifier.predict(data['data'][-30:])

# comparing predicted and original labels
print(
    f"\nPredicted labels - {predicted_category}\n\n\nOriginal labels - {data['target'][-30:]}\n\n"
)

print(f"Prdicted value: {classifier.predict([data['data'][-100]])} | Original value - {data['target'][-100]}")