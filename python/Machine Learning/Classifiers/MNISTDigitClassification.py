from sklearn.datasets import fetch_openml
import matplotlib
import matplotlib.pyplot as plt

mnist = fetch_openml('mnist_784')

x, y = mnist['data'], mnist['target']

# print(x)

digit = x.keys()
print(digit)
# digitImage = digit.reshape(28, 28)
#
# plt.imshow(digitImage, cmap=matplotlib.cm.binary, interpolation="nearest")

# print(mnist)
print(x.shape)
