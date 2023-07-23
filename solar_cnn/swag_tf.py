
#%%
from PIL import Image, ImageDraw
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import tensorflow as tf

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
x = np.array([1,2,3,4, 5, 6, 7])
y = 2*x
ax.plot(x, y)
plt.show()

#%%
path_image = 'data/test_data/145 N Mall Dr UNIT 29, St. George, UT 84790.png'
image = Image.open(path_image)
image = image.resize((400, 400))

image_array = np.array(image)
# image_array = np.expand_dims(image_array, axis=0)
image_tensor = tf.convert_to_tensor(image_array)
image_tensor

#%%
coordinates = [
    (160, 400-145),
    (128, 400-278),
    (276, 400-277),
    (276, 400-148),
    ]
coordinates_list = [
    160, 400-145,
    128, 400-278,
    276, 400-277,
    276, 400-148,
    ]
draw = ImageDraw.Draw(image)
draw.polygon(coordinates, outline = 'black', width = 1)
image
coordinates_list

#%%

# Define the CNN model
# model = tf.keras.models.Sequential([
#     tf.keras.layers.experimental.preprocessing.Rescaling(1./255, input_shape=(400, 400, 4)),
#     # tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
#     # tf.keras.layers.MaxPooling2D((2, 2)),
#     # tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
#     # tf.keras.layers.MaxPooling2D((2, 2)),
#     # tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
#     # tf.keras.layers.MaxPooling2D((2, 2)),
#     tf.keras.layers.Flatten(),
#     # tf.keras.layers.Dense(32, activation='relu'),
#     tf.keras.layers.Dense(4, activation='relu'),
#     tf.keras.layers.Dense(2, activation='sigmoid')
# ])

model = tf.keras.models.Sequential([
    # tf.keras.layers.experimental.preprocessing.Rescaling(1./255, input_shape=(2, 2, 1)),
    # tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(8, input_shape = [1]),
    tf.keras.layers.Dense(1),
])

# Compile the model
model.compile(optimizer='sgd',
              loss='mean_squared_error')

# Print the model summary
model.summary()

# y = np.array([200,200])
# list(sum(coordinates, ()))
# %%
# x = np.array([1,2,3,4,5,6,7])
x = np.array([1,2,3,4, 5, 6, 7])
y = 2*x
y
data = pd.DataFrame({
    'x':x,
    'y':y,
})
data

#%%
model.fit(x, y, epochs=500)

# %%
model.predict([5, 10])


#%%
import tensorflow as tf
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
y = 2*x
y
print(x)
print(y)

#%%
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1]),
])

model.compile(optimizer='sgd', loss = 'mean_squared_error')


# %%
model.fit(x, y, epochs = 500)

# %%

model.predict([8])

#%%
