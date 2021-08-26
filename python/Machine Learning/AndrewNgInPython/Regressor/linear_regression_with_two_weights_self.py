import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


class LinearRegressionWithTwoWeights:
    def __init__(
        self,
        features,
        labels,
        alpha=0.01,
        initial_theta_1=0.1,
        initial_theta_0=0.2,
        debug=False,
    ):
        self.features = features
        self.labels = labels
        self.theta_1 = initial_theta_1
        self.theta_0 = initial_theta_0
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

        if not isinstance(self.theta_1, float):
            raise ValueError("initial_theta_1 must be a float")

    def eq_line(self, x):
        return self.theta_0 + self.theta_1 * x

    def abline(self, slope, intercept):
        axes = plt.gca()
        x_vals = np.array(axes.get_xlim())
        y_vals = intercept + slope * x_vals
        plt.plot(x_vals, y_vals, "--")

    def fit(self):
        """
        Hypothesis function:
            h(x) = θ_0 + θ_1 * x
        Cost function:
            (1/2m)(Σ((h_i(x) - y_i) ** 2))
        Gradient descent algorithm:
            θ_0 -= α * ∂(J(θ_0, θ_1))/∂θ_0
            θ_1 -= α * ∂(J(θ_0, θ_1))/∂θ_1
        where:
            ∂(J(θ_0, θ_1))/∂θ = (1/m) * (Σ(h_i(θ) - y_i))
            ∂(J(θ_0, θ_1))/∂1 = (1/m) * (Σ(h_i(θ) - y_i)) * x_i
        """
        self.run_fit = True
        while True:
            d_costd_theta_1 = sum(
                [x * (self.eq_line(x) - y) for x, y in zip(self.features, self.labels)]
            )
            d_costd_theta_0 = sum(
                [(self.eq_line(x) - y) for x, y in zip(self.features, self.labels)]
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
            temp_0 = self.theta_0 - self.alpha * (1 / self.m) * d_costd_theta_0
            temp_1 = self.theta_1 - self.alpha * (1 / self.m) * d_costd_theta_1
            self.theta_0 = temp_0
            self.theta_1 = temp_1

            if self.debug:
                print(
                    f"theta_0: {self.theta_0} | theta_1: {self.theta_1} | Cost function: {self.cost_function} | Cost Prev: {self.cost_prev}"
                )

            if abs(self.cost_prev - self.cost_function) < 1e-3:
                break
            else:
                self.cost_prev = self.cost_function

        print(f"\nFitted line: y = {self.theta_0} + {self.theta_1} * x")

    def mse(self, true_values, predicted_values):
        return mean_squared_error(true_values, predicted_values)

    def plot(self):
        if not self.run_fit:
            print("\nIn order to fit the data, please run the fit method.\n")
        plt.scatter(self.features, self.labels)
        self.abline(self.theta_1, self.theta_0)
        plt.show()

    def predict(self, test_values):

        predicted_values = np.array([])
        for value in test_values:
            predicted_values = np.append(
                predicted_values, self.theta_0 + self.theta_1 * value
            )

        return predicted_values


if __name__ == "__main__":

    data = datasets.load_diabetes()
    data_one_feature = np.array([x[2] for x in data.data])
    feature_train = data_one_feature[:-30]
    labels_train = data["target"][:-30]

    feature_test = data_one_feature[-30:]

    linear_regression = LinearRegressionWithTwoWeights(
        feature_train, labels_train, alpha=1.0, debug=True
    )
    linear_regression.fit()
    labels_predicted = linear_regression.predict(feature_test)

    print(
        f"Predicted value = {labels_predicted} | Original value = {data['target'][-30:]}\n\n"
    )

    print(f"MSE: {linear_regression.mse(data['target'][-30:], labels_predicted)}")

    linear_regression.plot()
