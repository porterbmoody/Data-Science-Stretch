#%%
from PIL import Image, ImageDraw
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from AIUtil import AIUtil
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Rescaling
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import image_dataset_from_directory
import os
import shutil


#%%
data_dir = 'data'
batch_size = 32
img_height = 100
img_width = 100
validation_split = .2
seed = 42

train_data = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=validation_split,
  subset="training",
  seed=seed,
  image_size=(img_height, img_width),
  batch_size=batch_size)

train_data

#%%

test_data = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=validation_split,
  subset="validation",
  seed=seed,
  image_size=(img_height, img_width),
  batch_size=batch_size)
test_data

for element in test_data.as_numpy_iterator():
  print(element)


#%%
# # for file in os.listdir('data/with_panels'):
#     # if file not in os.listdir('data/without_panels'):
#         # if file not in os.listdir('data/unused'):
#             # shutil.move('data/with_panels/'+file,'data/unused/unused_with_panels/'+file)
#             # print(file)
#         # shutil.move('data/unused/'+file, 'data/without_panels/'+file)
# data_generator = ImageDataGenerator(rescale = 1/255)

# image_path = 'data'
# data_generator = data_generator.flow_from_directory(
#     image_path,
#     target_size=(100, 100),
#     # train_dir,
# )
# data_generator

#%%

# build model
input_shape = (100,100,3)
model = Sequential()
model.add(Rescaling(scale=1.0/255.0, input_shape=input_shape))
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape = input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(32))
model.add(Dense(32, activation='sigmoid'))
model.add(Dense(1))

# Compile the model with appropriate optimizer and loss function
loss = 'mean_squared_error'
optimizer = 'sgd'
metrics=['accuracy']
model.compile(optimizer=optimizer, loss=loss, metrics = metrics)

# Print the model summary
model.summary()

#%%
epochs=10
model.fit(
  train_data,
  validation_data=test_data,
  epochs = epochs
)


#%%
# Evaluate the model on the test dataset
evaluation_result = model.evaluate(test_data)
evaluation_result

#%%

test = np.array([
    [[1,1],[1,1]],
    # [[2,2],[2,2]],
    ])
model.predict(test)

#%%
coordinates = [
    (160, 143),
    (126, 279),
    (277, 277),
    (276, 143)]
# coordinates =
coordinates = AIUtil.invert_coordinates(coordinates, image)
coordinates
y = np.array([[160, 257]])

# coordinates = AIUtil.preprocess_coordinates(coordinates, image)

#%%

draw = ImageDraw.Draw(image)
draw.polygon(coordinates, outline = 'black', width = 1)
image

#%%
coordinates = AIUtil.flatten_coordinates(coordinates)

#%%
image = Image.open(path_image)
image = image.resize((100, 100))
image_array = np.array(image)
image_array
# image_array = np.expand_dims(image_array, axis=0)
# image_tensor = np.array(tf.convert_to_tensor(image_array))
# image_tensor

#%%
x = np.array([
    [[174, 176, 166, 255],
     [177, 180, 167, 255],
     [179, 185, 176, 255],
     ]
    ])

# x = image_tensor.flatten()
y = np.array([
    [4],
    [8],
    [12],
    [16],
    [20],
    [24],
    ])
print(x)
print(y)

#%%
x = tf.stack(image_array)
y = np.array([
    [10]
])
x
y

#%%
num_classes = 5

model = tf.keras.Sequential([
  tf.keras.layers.Rescaling(1./255),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(num_classes)
])

#%%
model.compile(
  optimizer='adam',
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])
# %%
model.build()
model.summary()

# %%
