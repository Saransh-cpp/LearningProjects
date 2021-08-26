import time
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt


class LinearRegressionWithOneFeature:
    def __init__(self, features, labels, alpha=0.01, initial_theta=0.0, debug=False):
        self.features = features
        self.labels = labels
        self.theta = initial_theta
        self.cost_prev = 0
        self.alpha = alpha
        self.m = len(self.features)
        self.debug = debug
        self.cost_function = (1 / (2 * self.m)) * (
            (sum([self.eq_line(x) - y for x, y in zip(self.features, self.labels)]))
            ** 2
        )
        self.run_fit = False

        if not isinstance(self.features, np.ndarray) or not isinstance(
            self.labels, np.ndarray
        ):
            raise ValueError("features and labels must be ndarrays")
        elif len(self.features) != len(self.labels):
            raise ValueError("features and labels must have the same length")

        if not isinstance(self.alpha, float):
            raise ValueError("alpha must be a float")

        if not isinstance(self.theta, float):
            raise ValueError("initial_theta must be a float")

    def eq_line(self, x):
        return self.theta * x

    def abline(self, slope, intercept):
        axes = plt.gca()
        x_vals = np.array(axes.get_xlim())
        y_vals = intercept + slope * x_vals
        plt.plot(x_vals, y_vals, "--")

    def fit(self):
        """
        Hypothesis function: h(x) = θ * x
        Cost function: (1/2m)(Σ((h_i(x) - y_i) ** 2))
        Gradient descent algorithm: θ -= α * ∂(J(θ))/∂θ
        where: ∂(J(θ))/∂θ = (1/m) * (Σ(h_i(θ) - y_i)) * x_i
        """
        self.run_fit = True
        while True:
            d_costd_theta = sum(
                [x * (self.eq_line(x) - y) for x, y in zip(self.features, self.labels)]
            )

            self.cost_function = (1 / (2 * self.m)) * (
                (
                    sum(
                        [
                            (self.eq_line(x) - y) ** 2
                            for x, y in zip(self.features, self.labels)
                        ]
                    )
                )
            )
            self.theta -= self.alpha * (1 / self.m) * d_costd_theta

            if self.debug:
                print(
                    f"theta: {self.theta} | Cost function: {self.cost_function} | Cost Prev: {self.cost_prev}"
                )

            if abs(self.cost_prev - self.cost_function) < 1e-3:
                break
            else:
                self.cost_prev = self.cost_function

        print(f"\nFitted line: y = {self.theta} * x")
        print(f"\nMSE: {self.cost_function}\n")

    def plot(self):
        if not self.run_fit:
            print("\nIn order to fit the data, please run the fit method.\n")
        # plt.xlim(0, 0.05)
        # plt.ylim(0, 0.05)
        # plt.gca().set_aspect('equal', adjustable='box')
        plt.scatter(self.features, self.labels)
        self.abline(self.theta, 0)
        plt.show()

    def predict(self, test_values):

        predicted_values = np.array([])
        for value in test_values:
            predicted_values = np.append(predicted_values, self.theta * value)

        return predicted_values


if __name__ == "__main__":
    x = np.array([6, 2, 2, 1, 7, 8, 6, 8, 7])
    y = np.array([4, 5, 1, 3, 2, 4, 3, 6, 9])
    # x = np.random.rand(100)
    # y = np.random.rand(100)

    # data = datasets.load_diabetes()
    # data_one_feature = np.array([x[2] for x in data.data])
    # feature_train = data_one_feature[:-30]
    # labels_train = data["target"][:-30]

    # feature_test = data_one_feature[-30:]

    # temp = [list(x) for x in zip(feature_train, labels_train)]

    # i = 0
    # while i < len(temp):
    #     if abs(temp[i][0]) != temp[i][0] or temp[i][1] < 0.0:
    #         temp.pop(i)
    #     else:
    #         i += 1

    # feature_train = np.array([x[0] for x in temp])
    # labels_train = np.array([x[1] for x in temp])

    linear_regression = LinearRegressionWithOneFeature(x, y, alpha=0.01, debug=True)
    linear_regression.fit()
    # labels_predicted = linear_regression.predict(feature_test)

    # print(
    #     f"Predicted value = {labels_predicted} | Original value = {data['target'][-30:]}\n\n"
    # )

    linear_regression.plot()
