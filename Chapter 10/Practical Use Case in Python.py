#Practical Use Case in Python

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

import tensorflow as tf
from tensorflow.keras import layers
import pandas as pd
import numpy as np
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical

iris = load_iris()
X = iris.data
Y = iris.target

encoder =  LabelEncoder()
Y = encoder.fit_transform(Y)

onehot_encoder=OneHotEncoder(sparse=False)
Y=Y.reshape(len(Y), 1)
Y=onehot_encoder.fit_transform(Y)


X_Train, X_Test, Y_Train, Y_Test = train_test_split(
 			X, Y, test_size = 0.3, random_state=100)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
  ])

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_Train, Y_Train, batch_size=50, epochs=100)


loss, accuracy = model.evaluate(X_Test, Y_Test, verbose=0)
print('Loss:', loss)
print('Accuracy:', accuracy)

Y_Pred = model.predict(X_Test)

actual = np.argmax(Y_Test,axis=1)
predicted = np.argmax(Y_Pred,axis=1)

print(f"Actual: {actual}")
print(f"Predicted: {predicted}")