import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
import FF
# from keras.utils.np_utils import to_categorical



## TODO: COMPLETELY CLEAN UP DATE BEFORE LOADING IN


# load data
root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'

opp_stats = pd.read_csv(root + 'data/opp_stats_2010_2020.csv')
team_stats = pd.read_csv(root + 'data/team_stats_2010_2020.csv')
tourn_stats = pd.read_csv(root + 'data/tourn_stats_2021.csv')
tourn_opp_stats = pd.read_csv(root + 'data/tourn_opp_stats_2021.csv')
wins = pd.read_csv(root + 'data/wins_2010_2020.csv')

stats = FF.four_factor(team_stats, opp_stats)
tourn_stats = FF.four_factor(tourn_stats, tourn_opp_stats)

# remove weird column
stats = stats.drop(columns=['Unnamed: 0'], axis=1)
tourn_stats = tourn_stats.drop(columns=['Unnamed: 0'], axis=1)

tourn_stats = tourn_stats.iloc[:,1:].to_numpy()
tourn_stats = np.asarray(tourn_stats).astype(np.float32)

# merge the wins and stats
stats = stats.merge(wins, on='School')

# feature and target sets
y = stats['Wins']

X = stats.drop(columns=['School','Wins','Seed','Unnamed: 0'])

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)


model = keras.Sequential(
    [
        layers.Dense(256, activation="relu", name="layer1", input_shape=(11,)),
        layers.Dense(128, activation="relu", name="layer2"),
        layers.Dense(64, activation="relu", name="layer3"),
        layers.Dense(32, activation="relu", name="layer4"),
        layers.Dense(11, name="layer5"),
    ]
)


# # to np array
# x_train = x_train.to_numpy()
# x_test = x_test.to_numpy()
# y_train = y_train.to_numpy()
# y_test = y_test.to_numpy()
#
# # Preprocess the data (these are NumPy arrays)
# x_train = x_train.reshape(60000, 784).astype("float32") / 255
# x_test = x_test.reshape(10000, 784).astype("float32") / 255
#
# y_train = y_train.astype("float32")
# y_test = y_test.astype("float32")
#
# # Reserve 10,000 samples for validation
# x_val = x_train[-10000:]
# y_val = y_train[-10000:]
# x_train = x_train[:-10000]
# y_train = y_train[:-10000]

model.compile(
    optimizer='rmsprop',  # Optimizer
    # Loss function to minimize
    loss=keras.losses.SparseCategoricalCrossentropy(),
    # List of metrics to monitor
    metrics=['accuracy'],
)

# y_train_onehot = to_categorical(y_train)
# y_test = y_train_onehot

print("Fit model on training data")
history = model.fit(
    x_train,
    y_train,
    batch_size=32,
    epochs=500,
    # We pass some validation for
    # monitoring validation loss and metrics
    # at the end of each epoch
    # validation_data=(x_val, y_val),
)

# Evaluate the model on the test data using `evaluate`
print("Evaluate on test data")
results = model.evaluate(x_test, y_test, batch_size=128)
print("test loss, test acc:", results)

# Generate predictions (probabilities -- the output of the last layer)
# on new data using `predict`
print("Generate predictions for 3 samples")
predictions = model.predict(tourn_stats)
print("predictions shape:", predictions.shape)
print(predictions)
