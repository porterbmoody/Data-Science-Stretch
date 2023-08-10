#%%
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import numpy as np



#%%
x = np.array([
    [[1,1], [2,2]],
    [[3,3], [4, 4]],
    [[5, 5], [6, 6]],
    [[7, 7], [8, 8]],
    [[9, 9], [10, 10]],
])

y = np.array([
    [6],
    [14],
    [22],
    [30],
    [38],
])

print('x:', x)
print('y:', y)

#%%
model = Sequential()
model.add(Dense(64, input_shape=(2, 2), activation='relu'))
model.add(Flatten())
model.add(Dense(64))
model.add(Dense(1))

# Compile the model with an optimizer and loss function
loss = 'mean_squared_error'
model.compile(optimizer='adam', loss=loss)

#%%
epochs = 1000
history = model.fit(x, y, epochs=epochs)

#%%
# test = np.array([[[1, 1], [2, 2]]])
# model.predict(test)
test = np.array([[[1, 1], [10, 10]]])
prediction = model.predict(test)
print(prediction)

#%%
data_history = pd.DataFrame(history.history)
data_history

# Assuming you have a pandas DataFrame named history_df
# with columns 'loss', 'accuracy', 'val_loss', 'val_accuracy', etc.

# Plot loss
plt.plot(data_history['loss'], label='Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.title('Training and Validation Loss')
plt.show()

# %%


import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Input data
x = np.array([
    [[1, 1], [2, 2]],
    [[3, 3], [4, 4]],
    [[5, 5], [6, 6]],
    [[7, 7], [8, 8]],
])

y = np.array([
    [1],
    [5],
    [9],
    [13],
])

print('x:', x)
print('y:', y)

#%%
# Create a neural network model
model = Sequential()
model.add(Dense(64, input_shape=(2, 2), activation='relu'))
model.add(Dense(64))
model.add(Dense(1))

# Compile the model with an optimizer and loss function
loss = 'mean_squared_error'
optimizer = 'adam'
model.compile(optimizer=optimizer, loss=loss)

#%%
# Fit the model
epochs = 500
history = model.fit(x, y, epochs=epochs)

#%%
# Making prediction
prediction = model.predict(np.array([
    [[1, 1], [2, 2]],
    [[3, 3], [4, 4]],
    ]))
print(prediction)


# %%
# Making prediction for a single 2x2 input
prediction = model.predict(np.array([[[1, 1], [2, 2]]]).reshape(1, 2, 2, 1))
print(prediction)
#%%



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

# data_dir = 'data'
# batch_size = 32
# img_height = 100
# img_width = 100
# validation_split = .3
# seed = 42

# train_data = tf.keras.utils.image_dataset_from_directory(
# 	data_dir,
# 	validation_split=validation_split,
# 	subset="training",
# 	seed=seed,
# 	image_size=(img_height, img_width),
# 	batch_size=batch_size)

# train_data

# #%%

# test_data = tf.keras.utils.image_dataset_from_directory(
# 	data_dir,
# 	validation_split=validation_split,
# 	subset="validation",
# 	seed=seed,
# 	image_size=(img_height, img_width),
# 	batch_size=batch_size)
# test_data

# for element in test_data.as_numpy_iterator():
	# print(element)
