''' Using the Diabetes dataset that is in scikit-learn, answer the questions below and create a scatterplot
graph with a regression line '''

from sklearn.model_selection import train_test_split
import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets

diabetes = datasets.load_diabetes()
# how many sameples and How many features?
print(diabetes.data.shape)


# What does feature s6 represent?
print(diabetes.DESCR)


X_train, X_test, y_train, y_test = train_test_split(
    diabetes.data, diabetes.target, random_state=11
)

# There are three steps to model something with sklearn
# 1. Set up the model
mymodel = LinearRegression()

# 2. Use fit to train your model
mymodel.fit(X_train, y_train)

# print out the coefficient
print(mymodel.coef_)

# print out the intercept
print(mymodel.intercept_)

# 3. Ue predict to test your model predictions
predicted = mymodel.predict(X_test)
expected = y_test

# create a scatterplot with regression line
plt.plot(expected, predicted, ".")
x = np.linspace(0, 330, 100)

plt.show()
