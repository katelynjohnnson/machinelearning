import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
# using pandas, bring the csv into a dataframe (read_csv)
nyc = pd.read_csv("ave_hi_nyc_jan_1895-2018.csv")
# head(3) visualizes the first 3 rows
print(nyc.head(3))

print(nyc.Data.values)
# -1 tells it to convert as many columns as you have to rows
# the 1 means one column
print(nyc.Data.values.reshape(-1.1))

X_train, X_test, y_train, y_test = train_test_split(
    nyc.Data.values.reshape(-1.1), nyc.Temperature.values, random_state=11
)

lr = LinearRegression()
lr.fit(X=X_train, y=y_train)

coef = lr.coef_
intercept = lr.intercept_

predicted = lr.predict(X_test)
expected = y_test

print(predicted[:20])
print(expected[:20])


def predict(x): return coef * x + intercept


print(predict(2025))

# names the axes and what the data will be
axes = sns.scatterplot(
    data=nyc,
    x='Date',
    y='Temperature',
    hue="Temperature",
    palette='winter',
    legend=False
)

axes.set_ylim(10, 70)


x = np.array([min(nyc.Date.values), max(nyc.Data.values)])
print(x)
y = predict(x)
print(y)

line = plt.plot(x, y)

plt.show()
