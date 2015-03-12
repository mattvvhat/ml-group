#!/usr/bin/python

import numpy as np
import matplotlib as mp

data = np.genfromtxt('ex1data1.txt', delimiter=",")


def hypothesis(theta, x):
    return theta[0] + theta[1] * x

def deriv_cost_function(theta, x, h):
    theta0 = theta1 = 0

    for x, y in data:
        theta0 += hypothesis(theta, x)
        theta1 += hypothesis(theta, x)*x

    theta0 *= h
    theta1 *= h

    return [theta0, theta1]

def cost_function(theta, data):
    summa = 0
    for x, y in data:
        summa += (hypothesis(theta, x) - y) ** 2.0
    return summa / 2.0 / len(data)


def gradient_descent(guess, data, n=1, h=0.0001):

    theta = guess[:]
    m = len(data)

    for i in range(n):
        for x, y in data:
            new_theta = theta[:]
            new_theta[0] = new_theta[0] - h * (hypothesis(theta, x) - y)
            new_theta[1] = new_theta[1] - h * (hypothesis(theta, x) - y) * x
            theta = new_theta
            # deriv_cost_function(theta, x, 

    return theta


# print cost_function((0, 0), data)
theta = gradient_descent([0, 0], data, 15000)

print theta
print cost_function(theta, data)

for x in [-0.5, 0, 0.5]:
    for y in [-0.5, 0, 0.5]:
        guess = [theta[0] + x, theta[1] + y]
        print (x, y), cost_function(guess, data)
