import numpy as np
from sklearn import datasets


class LogisticRegression:
    """
    Logistic Regression using neural network.
    
    Parameters
    ==========
    X : np.ndarray
        Features to train a model. Should be of the form - 
        [
            [feature1dataset1, feature1dataset2, .... feature1datasetn],
            [feature2dataset1, feature2dataset2, .... feature2datasetn],
            [feature3dataset1, feature3dataset2, .... feature3datasetn],
        ]
    Y : np.ndarray
        Labels to train the model. Should be of the form -
        [
            [label1],
            [label2],
            [label3]
        ]
    alpha : numerical (optional)
        The learning rate to be used.
    """
    def __init__(self, X, Y, alpha=0.05):
        self.X = X
        self.Y = Y
        self.alpha = alpha
        self.m = len(self.X)

    def fit(self):
        self.J = 0
        self.J_last = 1
        dW = np.zeros(shape=(self.m, 1))
        self.b = 0
        self.W = np.zeros(shape=(self.m, 1))

        while True:
            Z = np.dot(self.W.T, self.X) + self.b
            A = np.array([self.sigmoid(x) for x in Z])
            dZ = A - self.Y
            dW = (1 / self.m) * (np.dot(self.X, dZ.T))
            db = (1 / self.m) * np.sum(dZ)

            self.J = -np.sum(
                np.multiply(self.Y.T, np.array([np.log(x) for x in A.T]))
                + np.multiply(1 - self.Y.T, np.array([np.log(1 - x) for x in A.T]))
            )

            self.W = self.W - self.alpha * dW
            self.b = self.b - self.alpha * db

            print(self.J)

            if abs(self.J - self.J_last) < 1e-3:
                break
            else:
                self.J_last = self.J

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def predict(self, x):
        prediction = []

        for single_data in x:
            print(self.sigmoid(np.dot(single_data, self.W) + self.b))
            prediction.append(
                1 if self.sigmoid(np.dot(single_data, self.W) + self.b) > 0.5 else 0
            )

        return prediction


if __name__ == "__main__":
    data = datasets.load_iris()

    x_train = data.data[:-60]
    y_train = data.target[:-60]

    model = LogisticRegression(x_train.T, np.array([y_train]))
    model.fit()
    print(model.predict(np.array([data.data[-100]])), data.target[-100])
