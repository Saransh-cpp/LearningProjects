from sklearn import datasets
from sklearn.linear_model import LogisticRegression

data = datasets.load_iris()

# training data
feature_train = data["data"][:-30]
labels_train = data["target"][:-30]

# testing features
feature_test = data["data"][-30:]

# fitting the data
model = LogisticRegression()
model.fit(feature_train, labels_train)

# predicting labes for the testing data
labels_predicted = model.predict(feature_test)

# comparing predicted and original labels
print(
    f"Predicted labels - {labels_predicted}\n\n\nOriginal labels - {data['target'][-30:]}\n\n"
)

# checking for a random value
print(
    f"Predicted value = {model.predict([data['data'][-30]])} | Predicted probability = {model.predict_proba([data['data'][-30]])} | Original value = {data['target'][-30]}\n"
)
