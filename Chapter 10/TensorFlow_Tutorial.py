#TensorFlow Tutorial

import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu',input_shape=[4])])

model.summary()