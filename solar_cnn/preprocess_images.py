#%%

from tensorflow.keras.preprocessing.image import ImageDataGenerator

image_dir = 'data/'
image_width = 400
image_height = 400
num_polygon_coordinates = 2
#%%
# Create an instance of ImageDataGenerator
datagen = ImageDataGenerator(rescale=1.0 / 255.0)  # Normalize pixel values between 0 and 1

# Prepare the data generator
batch_size = 32
input_shape = (image_width, image_height)
num_classes = num_polygon_coordinates * 2  # Replace with the appropriate number of coordinates

data_generator = datagen.flow_from_directory(
    directory=image_dir,
    classes=None,
    class_mode=None,
    batch_size=batch_size,
    target_size=input_shape,
    shuffle=True,
)

# Note that we set class_mode to None since we're not using traditional class labels.


#%%
