#%%
import tensorflow as tf
print("TensorFlow version:", tf.__version__)

from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model

tf.random.set_seed(42)

#%%

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Add a channels dimension
x_train = x_train[..., tf.newaxis].astype("float32")
x_test = x_test[..., tf.newaxis].astype("float32")

#%%
train_ds = tf.data.Dataset.from_tensor_slices(
    (x_train, y_train)).shuffle(10000).batch(32)

test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

test_ds

#%%

class MyModel(Model):
  def __init__(self):
    super(MyModel, self).__init__()
    self.conv1 = Conv2D(32, 3, activation='relu')
    self.flatten = Flatten()
    self.d1 = Dense(128, activation='relu')
    self.d2 = Dense(10)

  def call(self, x):
    x = self.conv1(x)
    x = self.flatten(x)
    x = self.d1(x)
    return self.d2(x)

# Create an instance of the model
model = MyModel()
model

#%%

loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

optimizer = tf.keras.optimizers.Adam()
optimizer
#%%
train_loss = tf.keras.metrics.Mean(name='train_loss')
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')

test_loss = tf.keras.metrics.Mean(name='test_loss')
test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy')
# %%
@tf.function
def train_step(images, labels):
  with tf.GradientTape() as tape:
    # training=True is only needed if there are layers with different
    # behavior during training versus inference (e.g. Dropout).
    predictions = model(images, training=True)
    loss = loss_object(labels, predictions)
  gradients = tape.gradient(loss, model.trainable_variables)
  optimizer.apply_gradients(zip(gradients, model.trainable_variables))

  train_loss(loss)
  train_accuracy(labels, predictions)
# %%
@tf.function
def test_step(images, labels):
  # training=False is only needed if there are layers with different
  # behavior during training versus inference (e.g. Dropout).
  predictions = model(images, training=False)
  t_loss = loss_object(labels, predictions)

  test_loss(t_loss)
  test_accuracy(labels, predictions)
# %%
EPOCHS = 5

for epoch in range(EPOCHS):
  # Reset the metrics at the start of the next epoch
  train_loss.reset_states()
  train_accuracy.reset_states()
  test_loss.reset_states()
  test_accuracy.reset_states()

  for images, labels in train_ds:
    train_step(images, labels)

  for test_images, test_labels in test_ds:
    test_step(test_images, test_labels)

  print(
    f'Epoch {epoch + 1}, '
    f'Loss: {train_loss.result()}, '
    f'Accuracy: {train_accuracy.result() * 100}, '
    f'Test Loss: {test_loss.result()}, '
    f'Test Accuracy: {test_accuracy.result() * 100}'
  )
# %%
import PIL.Image
import tensorflow as tf
import numpy as np

image_size = (400, 400)
batch_size = 20
data_dir = 'data/'
train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=image_size,
  batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=image_size,
  batch_size=batch_size)

train_ds.class_names

#%%
normalization_layer = tf.keras.layers.Rescaling(1./255)
normalization_layer


#%%



normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
# Notice the pixel values are now in `[0,1]`.
print(np.min(first_image), np.max(first_image))


#%%

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
  tf.keras.layers.Dense(2)
])

model.compile(
  optimizer='adam',
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

#%%
model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=10
)

# %%

val_size = int(image_count * 0.2)
train_ds = list_ds.skip(val_size)
val_ds = list_ds.take(val_size)


#%%
from tensorflow import keras

x = [-1, 0, 1, 2, 3, 4]
y = [-3, -1, 1, 3, 5, 7]

x
#%%

model = tf.keras.Sequential([
    layers.Dense(3, activation='relu', input_dim=input_dim),
    layers.Dense(1, activation='softmax')
])
model.compile(optimizer='adam',
		loss = ['mean_squared_error'])


model.fit(x, y, epochs=500)

#%%
import tensorflow as tf
from tensorflow.keras import layers
import numpy as np

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Set random seed for reproducibility
tf.random.set_seed(42)
# Generate some dummy data for training
# Replace this with your own data loading and preprocessing code
input_dim = 2
x = np.array([[1,1], [2,2]])
# train_data = np.random.random((4, input_dim))
y = np.array([[2,2], [4,4]])
print(x)
print(y)

#%%

# Create the model architecture
model = tf.keras.Sequential([
    layers.Dense(units=64, input_shape=[2]),
    layers.Dense(units=128, input_shape=[1]),
    layers.Dense(2)  # Output layer with 1 node for regression
])

# Compile the model
model.compile(optimizer='adam',
              loss='mean_squared_error')


# Train the model
model.fit(x, y, epochs=500, batch_size=32)



#%%
model.predict([[3, 3]])

# Generate some dummy data for testing
# Replace this with your own test data
# test_data = np.random.random((20, input_dim))

# Make predictions using the trained model
# predictions = model.predict(test_data)

# Print the predicted values
# print(predictions)


# %%

import tensorflow as tf
data_dir = 'data/test_data/'
image_size = (400, 400)
batch_size = 20
train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=image_size,
  batch_size=batch_size)

train_ds
#%%
from PIL import Image
import numpy as np
import tensorflow as tf

path_image = 'data/test_data/145 N Mall Dr UNIT 29, St. George, UT 84790.png'
image = Image.open(path_image)
image = image.resize((400, 400))

np_array_image = np.array(image)

image_tensor = tf.convert_to_tensor(np_array_image)
image_tensor


#%%

# Define the CNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(400, 400, 4)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy')

# Print the model summary
model.summary()

#%%
y = np.array([200,200])

model.fit()
