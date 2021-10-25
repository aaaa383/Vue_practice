import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pickle
## GETTING AND PARSING THE DATA


training_data = load_iris()


X = training_data.data
y = training_data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

logreg = LogisticRegression(solver="liblinear", multi_class="ovr")
clf = logreg.fit(X_train, y_train)

print("Score: ", clf.score(X_test, y_test))
pickle.dump(clf, open("../models/model.pkl", "wb"))

