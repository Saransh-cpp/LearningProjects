import pickle

# Pickling a python object
cars = ["Audi", "BMW", "Maruti Suzuki"]
file = "mycar.pkl"
fileobj = open(file, "wb")
pickle.dump(cars, fileobj)
fileobj.close()

file = "mycar.pkl"
fileobj = open(file, "rb")
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
