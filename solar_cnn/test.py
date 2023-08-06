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
