import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

data = datasets.load_diabetes()

# use only 1 feature (for plotting / visualisation)
print("\n===========================Using only 1 feature================================\n")
data_one_feature = data.data[:, np.newaxis, 2]

# training data
feature_train = data_one_feature[:-30]
labels_train = data["target"][:-30]

# testing features
feature_test = data_one_feature[-30:]

# fit the data
model = LinearRegression()
model.fit(feature_train, labels_train)

# predicting labes for the testing data
labels_predicted = model.predict(feature_test)

# comparing predicted and original labels
print(
    f"Predicted labels - {labels_predicted}\n\n\nOriginal labels - {data['target'][-30:]}\n\n"
)

# calculating mean squared error
mse = mean_squared_error(data['target'][-30:], labels_predicted)
print(f"MSE = {mse}\n\n")

# plotting the data
plt.scatter(feature_train, labels_train)
plt.plot(feature_test, labels_predicted)
plt.show()

# checking for a random value
print(
    f"Predicted value = {model.predict([data_one_feature[-30]])} | Original value = {data['target'][-30]}\n\n"
)

# use all features
print("\n===========================Using all features================================\n")

# training data
feature_train = data['data'][:-30]
labels_train = data['target'][:-30]

# testing features
feature_test = data['data'][-30:]

# fitting the data
model = LinearRegression()
model.fit(feature_train, labels_train)

# predicting labes for the testing data
labels_predicted = model.predict(feature_test)

# comparing predicted and original labels
print(
    f"Predicted labels - {labels_predicted}\n\n\nOriginal labels - {data['target'][-30:]}\n\n"
)

# calculating mean squared error
mse = mean_squared_error(data['target'][-30:], labels_predicted)
print(f"MSE = {mse}\n\n")

# checking for a random value
print(f"Predicted value = {model.predict([data['data'][-30]])} | Original value = {data['target'][-30]}\n\n")
