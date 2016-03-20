import numpy as np
import matplotlib.pyplot as plt

def calccost(theta, m, X, y):
    pred = np.dot(X, theta)
    return (1./(2*m))*(np.sum(np.square(pred-y)))

data = []
m = 0

filename = raw_input("Please enter a filename to get data from:")

with open(filename, 'rb') as csvfile:
    import csv
    datafile = csv.reader(csvfile, delimiter=',')
    for row in datafile:
        m += 1
        data.append(row)

data = np.array(data, dtype='float64')
x = data[:,0]
y = data[:,1].reshape(m, 1)

X = np.transpose([np.ones(m), x])
theta = np.dot(np.dot(np.linalg.pinv(np.dot(np.transpose(X), X)), np.transpose(X)), y)
print("Theta using the normal equation:")
print(theta)
plt.figure(1)

plt.subplot(121)
plt.title("Normal Equation\n")
plt.ylabel("Profit in $10,000s")
plt.xlabel("Population of City in 10,000s")
plt.plot(x, y, 'rx')
plt.plot(x, np.dot(X, theta))

prevtheta = theta = np.array([[0.],[0.]])

theta = theta - 0.01*((1./m)*np.sum((np.dot(X, theta)-y)*X, axis=0)).reshape(2,1);

while calccost(prevtheta, m, X, y) != calccost(theta, m, X, y):
    prevtheta = theta
    theta = theta - 0.01*((1./m)*np.sum((np.dot(X, theta)-y)*X, axis=0)).reshape(2,1);

print("Theta using gradient descent:")
print(theta)

plt.subplot(122)
plt.title("Gradient Descent\n")
plt.ylabel("Profit in $10,000s")
plt.xlabel("Population of City in 10,000s")
plt.plot(x, y, 'rx')
plt.plot(x, np.dot(X, theta))

plt.show()