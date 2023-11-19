import tensorflow as tf
from tensorflow.keras import layers, models



model = models.Sequential()
model.add(layers.Flatten())
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(1, activation='softmax'))

data1['mileage']

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

train_data = data['']
validation_data = ... # Load and preprocess validation data

history = model.fit(train_data, epochs=num_epochs, validation_data=validation_data)

test_data = ... # Load and preprocess test data
test_loss, test_acc = model.evaluate(test_data)

predictions = model.predict(test_data)
