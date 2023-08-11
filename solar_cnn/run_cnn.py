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

image_paths =  os.listdir('data/without_panels')
image_size = (200,200)

image_tensors = []
# load images in folder as tensors
for image_path in image_paths:
	path = 'data/without_panels/' + image_path
	image_tensor = AIUtil.load_image_tensor(path, image_size)
	image_tensors.append(image_tensor)

image_tensors


#%%
image = Image.open('data/without_panels/' + image_paths[5]).convert('RGB')
image = image.resize(image_size)

draw = ImageDraw.Draw(image)
coordinates = [(65, 73),(100, 100)]# ]
coordinates = AIUtil.invert_coordinates(coordinates, image_size)
draw.line(coordinates)
image


#%%
data_coordinates = pd.DataFrame({
	'address':image_paths[0],
	'coordinates':[
		[78, 62], 
		[64, 62],
		[55, 75],
		[59, 69],
		[55, 69],
		],
})

data_coordinates
# coordinates = np.array([
	# [70, 71],
	# [62, 74],
	# [56, 68],
	# [73, 75],
	# [71, 76],
	# ])


#%%

# build model
input_shape = (200,200,4)
model = Sequential()
model.add(Rescaling(scale=1.0/255.0, input_shape=input_shape))
# model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape = input_shape))
# model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(32))
model.add(Dense(32, activation='sigmoid'))
model.add(Dense(2))

# Compile the model with appropriate optimizer and loss function
loss = 'mean_squared_error'
optimizer = 'sgd'
model.compile(optimizer=optimizer, loss=loss)

# Print the model summary
model.summary()

#%%
x = np.array([
	image_tensors[0],
	image_tensors[1],
	image_tensors[2],
	image_tensors[3],
	image_tensors[4],
	image_tensors[5],
	])
# x = tf.reshape(x, (1, 200, 200, 4))
y = np.array(list(data_coordinates['coordinates']))

print(x.shape)
print(y.shape)

#%%
epochs=25
batch_size = 1
model.fit(
	x,
	y,
	epochs = epochs,
	batch_size = batch_size
)

#%%
# Evaluate the model on the test dataset

test = image_tensors[3]
test = tf.reshape(test, (1, 200, 200, 4))
test.shape
#%%
model.predict(test, batch_size = batch_size)

# %%
