#%%
import tensorflow as tf
from tensorflow.keras import layers

#%%

# Define the CNN model
model = tf.keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))


#%%

import numpy as np
import tensorflow as tf
import trimesh

import tensorflow_graphics.geometry.transformation as tfg_transformation
from tensorflow_graphics.notebooks import threejs_visualization

# Download the mesh.
!wget https://storage.googleapis.com/tensorflow-graphics/notebooks/index/cow.obj
# Load the mesh.
mesh = trimesh.load("cow.obj")
mesh = {"vertices": mesh.vertices, "faces": mesh.faces}
# Visualize the original mesh.
threejs_visualization.triangular_mesh_renderer(mesh, width=400, height=400)
# Set the axis and angle parameters.
axis = np.array((0., 1., 0.))  # y axis.
angle = np.array((np.pi / 4.,))  # 45 degree angle.
# Rotate the mesh.
mesh["vertices"] = tfg_transformation.axis_angle.rotate(mesh["vertices"], axis,
                                                        angle).numpy()
# Visualize the rotated mesh.
threejs_visualization.triangular_mesh_renderer(mesh, width=400, height=400)