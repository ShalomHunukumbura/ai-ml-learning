import numpy as np

arr = np.array([1,2,3,4])

print(arr)
print(type(arr))

print("\n\n\n")

data = np.array([
	[78,32,12],
	[98,49,83],
	[87,79,31]
])

print(data)
print(data.shape)
print("\n\n")

print(data[0]) # first row
print(data[:, 0]) # first column

print("\n\n")

a = np.array([1,2,3])
b = np.array([4,5,6])

print("a: ", a)
print("b: ",b)
print(a+b)
print(a*b)

print("\n\n\n\nprediction")

features = np.array([5,80])
weights = np.array([0.5,0.3])

predictions = np.dot(features, weights)

print("prediction: ", predictions)

print("\n\n Broadcasting")

arr = np.array([1,2,3])
print(arr+10)
