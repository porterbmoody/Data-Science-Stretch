#%%
from PIL import Image, ImageDraw
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from AIUtil import AIUtil
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import image_dataset_from_directory
import os
import shutil
import ast

pd.set_option('display.max_colwidth', None)

path = 'data/without_panels/'
path_coordinates = 'data_coordinates.csv'

data_coordinates = pd.read_csv(path_coordinates, converters={'coordinates': ast.literal_eval})

data_coordinates

#%%
image_size = (200,200)

image_tensors = AIUtil.load_image_tensors(data_coordinates['address'], image_size)
image_tensors
print('image tensors:',len(image_tensors))
print('shape:', image_tensors[0].shape)

#%%
x = np.array(image_tensors)
# x = tf.reshape(x, (1, 200, 200, 4))
y = np.array(list(data_coordinates['coordinates']))

print(x.shape)
print(y.shape)


#%%

# build model
input_shape = (200,200,4)
model = Sequential()
model.add(Rescaling(scale=1.0/255.0, input_shape=input_shape))
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape = input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(64))
model.add(Dense(64, activation='sigmoid'))
model.add(Dense(2))

# Compile the model with appropriate optimizer and loss function
loss = 'mean_squared_error'
optimizer = 'sgd'
model.compile(optimizer=optimizer, loss=loss)

# Print the model summary
model.summary()

#%%
epochs=50
batch_size = 1
history = model.fit(
	x,
	y,
	epochs = epochs,
	batch_size = batch_size
)

#%%
plt.plot(history.history['loss'])

#%%

test = image_tensors[1]
test = tf.reshape(test, (1, 200, 200, 4))
test.shape

model.predict(test, batch_size = batch_size)

# %%

# coordinates = np.array([
	# [70, 71],
	# [62, 74],
	# [56, 68],
	# [73, 75],
	# [71, 76],
	# ])

# data_coordinates = pd.DataFrame({
# 	'address':image_paths[:11],
# 	'coordinates':[
# 		[78, 62],
# 		[64, 62],
# 		[55, 75],
# 		[59, 69],
# 		[55, 69],
# 		[55, 69],
# 		[78, 75],
# 		[79, 73],
# 		[68, 70],
# 		[62, 75],
# 		[56, 71],
# 		],
# })