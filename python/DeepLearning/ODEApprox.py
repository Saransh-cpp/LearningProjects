import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt


physical_devices = tf.config.list_physical_devices("GPU")
tf.config.experimental.set_memory_growth(physical_devices[0], True)


def f(x):
    return 2 * x


def get_model():
    model = keras.Sequential(
        [
            keras.layers.Dense(32, input_shape=(1,), activation="relu"),
            keras.layers.Dense(32, activation="relu"),
            keras.layers.Dense(1, activation="sigmoid"),
        ]
    )

    return model


model = get_model()

model.compile(
    optimizer=tf.optimizers.SGD(1),
    loss=keras.losses.MeanSquaredError(),
    # metrics=["accuracy"],
)

model.fit([1, 2, 3], [f(1), f(2), f(3)], epochs=10)

model.evaluate([4, 5, 6], [f(4), f(5), f(6)])

print(model.predict([7]))

# f0 = 1
# inf_s = np.sqrt(np.finfo(np.float32).eps)
# learning_rate = 0.01
# training_steps = 5000
# batch_size = 100
# display_step = 500
# # Network Parameters
# n_input = 1  # input layer number of neurons
# n_hidden_1 = 32  # 1st layer number of neurons
# n_hidden_2 = 32  # 2nd layer number of neurons
# n_output = 1  # output layer number of neurons
# weights = {
#     "h1": tf.Variable(tf.random.normal([n_input, n_hidden_1])),
#     "h2": tf.Variable(tf.random.normal([n_hidden_1, n_hidden_2])),
#     "out": tf.Variable(tf.random.normal([n_hidden_2, n_output])),
# }
# biases = {
#     "b1": tf.Variable(tf.random.normal([n_hidden_1])),
#     "b2": tf.Variable(tf.random.normal([n_hidden_2])),
#     "out": tf.Variable(tf.random.normal([n_output])),
# }
# # Stochastic gradient descent optimizer.
# optimizer = tf.optimizers.SGD(learning_rate)

# # Create model
# def multilayer_perceptron(x):
#     x = np.array([[[x]]], dtype="float32")
#     layer_1 = tf.add(tf.matmul(x, weights["h1"]), biases["b1"])
#     layer_1 = tf.nn.sigmoid(layer_1)
#     layer_2 = tf.add(tf.matmul(layer_1, weights["h2"]), biases["b2"])
#     layer_2 = tf.nn.sigmoid(layer_2)
#     output = tf.matmul(layer_2, weights["out"]) + biases["out"]
#     return tf.nn.sigmoid(output)


# # Universal Approximator
# def g(x):
#     return x * multilayer_perceptron(x) + f0


# # Given EDO
# def f(x):
#     return 2 * x


# # Custom loss function to approximate the derivatives
# def custom_loss():
#     summation = []
#     for x in np.linspace(-1, 1, 10):
#         dNN = (g(x + inf_s) - g(x)) / inf_s
#         summation.append((dNN - f(x)) ** 2)
#     return tf.sqrt(tf.reduce_mean(tf.abs(summation)))


# def train_step():
#     with tf.GradientTape() as tape:
#         loss = custom_loss()
#     trainable_variables = list(weights.values()) + list(biases.values())
#     gradients = tape.gradient(loss, trainable_variables)
#     optimizer.apply_gradients(zip(gradients, trainable_variables))


# # Training the Model:
# for i in range(training_steps):
#     train_step()
#     if i % display_step == 0:
#         print("loss: %f " % (custom_loss()))

# # True Solution (found analitically)
# def true_solution(x):
#     return x ** 2 + 1


# X = np.linspace(0, 1, 100)
# result = []
# for i in X:
#     result.append(g(i).numpy()[0][0][0])
# S = true_solution(X)
# plt.plot(X, result)
# plt.plot(X, S)
# plt.show()
