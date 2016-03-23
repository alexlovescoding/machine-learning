import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1./(1+np.exp(-z))

def prediction(theta, X):
    return sigmoid(np.dot(X, theta))

def costFunction(theta, *args):
    X, y = args
    m = len(y)
    pred = prediction(theta, X)
    return (-1./m)*np.sum(y*np.log(pred)+(1-y)*np.log(1-pred));

def gradient(theta, *args):
    X, y = args
    m = len(y)
    pred = prediction(theta, X)
    return (1./m)*np.sum((pred-y).reshape(len(pred),1)*X, axis=0)

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
x = data[:,[0,1]]
y = data[:,2]

pos = np.where(y==1)[0]
neg = np.where(y==0)[0]

plt.xlabel('Exam 1 score')
plt.ylabel('Exam 2 score')

plt.plot(x[pos,0], x[pos,1], 'rx', label='Admitted')
plt.plot(x[neg,0], x[neg,1], 'yo', label='Not Admitted')

X = np.ones((m,3))
X[:,[1,2]] = x
inittheta = np.ones((len(X[1,:])))
args = (X, y)
theta = optimize.fmin_cg(costFunction, inittheta, fprime=gradient, args=args)
plot_x = np.array([np.amin(X[:,1])-2, np.amax(X[:,1])+2])
plot_y = (-1./theta[2])*(theta[1]*plot_x + theta[0])
plt.plot(plot_x, plot_y, label='Decision Boundary')
plt.legend(loc='upper right')
plt.show()