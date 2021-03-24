import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


# Specify root folder
ROOT = '/Users/christiangeer/bracketlytics/new_model/'

# Read in csv file and remove unecessary F1 column
data = pd.read_csv(ROOT + 'data/joined_data.csv')
data = data.drop("F1", axis=1)
print(data)
# Split data into attributes and lables
X = data.iloc[:,1:9].values
y = data.iloc[:, 9].values

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Feature sclaing
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Training KNN algorithm
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Evaluate the algorithm
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
