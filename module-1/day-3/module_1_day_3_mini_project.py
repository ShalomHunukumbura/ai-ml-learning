import numpy as np

# features: hours studied, attendance
x = np.array([
	[2,60],
	[4,70],
	[6,80],
	[8,90]
])

print(x)

# weights(model parameters)
weights = np.array([0.5,0.3])

# predictions
predictions = np.dot(x,weights)

print("\n\n\nPrediction\n\n", predictions)
