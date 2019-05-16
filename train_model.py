#!/usr/bin/env python

import numpy as np
from tensorflow.keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import plot_model

# https://keras.io/models/sequential/
model = Sequential()

# https://keras.io/layers/convolutional/#conv2d
# keras.layers.Conv2D(filters, kernel_size, strides=(1, 1), padding='valid', data_format=None, dilation_rate=(1, 1), activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
model.add(Conv2D(filters=32, kernel_size=5, data_format="channels_last", activation="relu", input_shape=(28, 28, 1)))
# https://keras.io/layers/convolutional/#conv2d
# keras.layers.Conv2D(filters, kernel_size, strides=(1, 1), padding='valid', data_format=None, dilation_rate=(1, 1), activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
model.add(MaxPooling2D(data_format="channels_last"))
model.add(Conv2D(filters=16, kernel_size=3, data_format="channels_last", activation="relu"))
model.add(MaxPooling2D(data_format="channels_last"))

# https://keras.io/layers/core/#flatten
# keras.layers.Flatten(data_format=None)
model.add(Flatten(data_format="channels_last"))

# https://keras.io/layers/core/#dense
# keras.layers.Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
model.add(Dense(units=128, activation="relu"))
model.add(Dense(units=64, activation="relu"))
model.add(Dense(units=4, activation="softmax"))

# https://keras.io/models/sequential/#compile
# compile(optimizer, loss=None, metrics=None, loss_weights=None, sample_weight_mode=None, weighted_metrics=None, target_tensors=None)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# https://keras.io/utils/#print_summary
# keras.utils.print_summary(model, line_length=None, positions=None, print_fn=None)
model.summary()

# https://keras.io/utils/#plot_model
# keras.utils.plot_model(model, to_file='model.png', show_shapes=False, show_layer_names=True, rankdir='TB', expand_nested=False, dpi=96)
plot_model(model, show_shapes=True)

x = np.load("./x.npy")
y = np.load("./y.npy")

# https://keras.io/models/sequential/#fit
# fit(x=None, y=None, batch_size=None, epochs=1, verbose=1, callbacks=None, validation_split=0.0, validation_data=None, shuffle=True, class_weight=None, sample_weight=None, initial_epoch=0, steps_per_epoch=None, validation_steps=None, validation_freq=1)
model.fit(x=x, y=y, batch_size=100, epochs=6, validation_split=0.2)

# https://keras.io/getting-started/faq/#savingloading-whole-models-architecture-weights-optimizer-state
model.save("model.h5")

