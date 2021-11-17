import matplotlib.pyplot as plt2
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
# for machine learning, the image used must be 1Dimensional
# load_digits takes the entire dataset and makes it into an object called digits
# digits is our dataset and is referred to as a bunch object
# three attributes:
# digits.data = contains all of the samples
# digits.target = tells what each sample represents (a number between 0 and 9)
# digits.images =
digits = load_digits()
#DESCR = describe
# print(digits.DESCR)

# [150] shows the 150th sample
print(digits.data[150])
print(digits.target[150])
# 1D = 64 columns in one row
# 2D = 8x8; columnsxrows
# first image(row) is a 0, then 1, then 2,etc. then it starts over after 9

# shows (rows,columns):
print(digits.data.shape)
# shows (rows,); only rows:
print(digits.target.shape)


# creates an empty chart of 24 pictures
# subplots makes smaller charts on one big chart
figure, axes = plt.subplots(nrows=4, ncolumns=6, figsize=(6, 4))
# plt.show()

# ravel: makes 2D into 1D; mkaes a (4x6) into (24x1)
for item in zip(axes.ravel(), digits.images, digits.target):
    axes, image, target = item
    axes.imshow(image, cmap=plt.cm.gray_r)
    # remove tick marks
    axes.set_xticks([])
    axes.set_yticks([])
    # set the title; usually named after the target
    axes.set_title()

# configures it into a better layout
plt.tight_layout()
# plt.show()

# splits into 4 different arrays

# picks 75% random rows for training and 25% for testing
# random_state = 11 splits the data exactly the same with other's
data_train, data_test, target_train, target_test = train_test_split(
    digits.data, digits.target, random_state=11
)

print(data_train.shape)  # training data so it is 2D and 75% of rows
print(data_test.shape)  # 25% of the rows
print(target_train.shape)  # 1D
print(target_test.shape)  # this is the answer to the target rows

# KNeighborsClassifier is the estimater that does the work for us
knn = KNeighborsClassifier()

# fit() algorithm that runs and does all of the machine learning
# X=data_train because we are training the data with fit
# telling is that the 75% rows each of the rows has a target...it looks at the numbers to look for the target value
knn.fit(X=data_train, y=target_train)
# we only have x because we provide the test (25%) values and it predicts the y based off of the test data
# two arrays:
predicted = knn.predict(X=data_test)
expected = target_test

# what the machine understood
print(predicted[:20])
# what we expect the machine to do
print(expected[:20])
# this gives the percentage it is predicted to have been right/accurate
# score method shows the accuracy
print(format(knn.score(data_test, target_test), ".2%"))

# which ones it got wrong
# takes both predicted(p) and expected(e) ad compares at the same time
# ignores if right but if p adn e dont match, it is put into a separate list
wrong = [(p, e) for (p, e) in zip(predicted, expected) if p != e]

print(wrong)

# allows us to see where it messed up
confusion = confusion_matrix(y_true=expected, y_pred=predicted)
print(confusion)

# making a data frame using 0 through 9
confusion_df = pd.Dataframe(confusion, index=range(10), columns=range(10))
# creates a colorscale heat map
figure = plt2.figure(figsize=(7, 6))
axes = sns.heatmap(confusion_df, annot=True, cmap=plt.cm.nipy_spectral_r)

plt2.show()
