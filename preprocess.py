#!/usr/bin/env python

from os import listdir

import numpy as np

from tensorflow.keras.utils import to_categorical

files = ['cat.npy', 'dog.npy', 'apple.npy', 'banana.npy']

x = np.concatenate([np.load(f)[:12000] for f in files]) / 255.0
y = np.concatenate([np.full(12000, i) for i in range(len(files))])

perm = np.random.permutation(len(x))
x = x[perm]
y = y[perm]

# (samples, rows, cols, channels)
x = x.reshape(x.shape[0], 28, 28, 1).astype('float32')
y = to_categorical(y)

np.save('./x.npy', x)
np.save('./y.npy', y)

