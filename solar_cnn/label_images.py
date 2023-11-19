#%%
from flask import Flask, render_template, request
from PanelFramework import PanelFramework
from RooftopImage import RooftopImage
from shapely.geometry import Polygon
from AIUtil import AIUtil
from PIL import Image, ImageDraw
import PIL
import os
import pandas as pd
from termcolor import colored
import tensorflow as tf

#%%

class GUI:

    def __init__(self, i, current_addresses) -> None:
        self.address = current_addresses[i]
        # print('pizza address', self.address)
        self.i = i
        self.current_addresses = current_addresses

        # self.address = address
        self.polygon_coordinates = []
        self.rooftop_image = RooftopImage(address)
        # print('pizza rooftop', self.rooftop_image.path_rooftop)
        print(self.rooftop_image.path_rooftop)

    def next_address(self):
        self.address = current_addresses[i + 1]
        self.polygon_coordinates.clear()
        del self.rooftop_image
        self.rooftop_image = RooftopImage(address)
        print(self.rooftop_image.path_rooftop)

app = Flask(__name__)

def return_updated():
    print('should be next path', gui.rooftop_image.path_rooftop)
    if hasattr(gui.rooftop_image, 'path_temp'):
        return render_template('index.html', address = gui.rooftop_image.address, path_rooftop=gui.rooftop_image.path_temp)
    return render_template('index.html', address = gui.rooftop_image.address, path_rooftop=gui.rooftop_image.path_rooftop)

@app.route('/')
def index():
    return return_updated()

@app.route('/image_click', methods=['POST'])
def image_click():
    # print(request.form)
    x = int(request.form['x'])
    y = int(request.form['y'])
    coordinates = (x, 600 - y)
    gui.polygon_coordinates.append(coordinates)
    print('gui.polygon_coordinates:', gui.polygon_coordinates)
    return return_updated()

@app.route('/submit', methods=['POST'])
def submit():
    print(gui.polygon_coordinates)
    polygon = Polygon(gui.polygon_coordinates)
    panel_framework = PanelFramework(polygon)
    gui.rooftop_image.add_panel_framework(panel_framework, draw_panels = True)
    # clear list so next polygon can be created
    gui.polygon_coordinates.clear()

    gui.rooftop_image.temp_save()
    return return_updated()

@app.route('/save_panel_frameworks', methods=['POST'])
def save_panel_frameworks():
    print('/save_panel_frameworks method')
    gui.rooftop_image.save_frameworks()
    return return_updated()

@app.route('/next_rooftop_image', methods = ['POST'])
def next_rooftop_image():
    gui.next_address()

    return return_updated()

@app.route('/clear', methods=['POST'])
def clear():
    gui.polygon_coordinates.clear()
    return return_updated()

if __name__ == '__main__':
    current_addresses = os.listdir('static/images/without_panels')
    for i, address in enumerate(current_addresses):
        if address.endswith('.png'):
            address = address[:-4]
            print(address)
        if address in list(set(pd.read_csv('static/images/panel_frameworks.csv')['address'])):
            print('address already exists:', address)
            continue
            # raise Exception('address already recorded', address)
        else:
            print(address)
            valid = input("is this valid(y/n):")
            print()
            if valid == 'y':
                gui = GUI(address)
                app.run()

# %%
path = 'data/without_panels/145 N Mall Dr UNIT 31, St. George, UT 84790.png'
image_size = (400, 400)
image = Image.open(path)
image = image.resize(image_size)
image

draw = ImageDraw.Draw(image)
coordinates = [(130, 145), (200,200)]
# coordinates = tf.reshape(tf.convert_to_tensor(coordinates), shape=(-1,))
# coordinates = list(sum(coordinates, ()))
coordinates

#%%
coordinates = AIUtil.invert_coordinates(coordinates, image_size)
draw.line(coordinates)

image

#%%

# Convert the PIL image to a TensorFlow tensor
tf_image = tf.convert_to_tensor(image)

# Print the shape and data type of the TensorFlow tensor
print("Tensor shape:", tf_image.shape)
print("Data type:", tf_image.dtype)

#%%
path = 'data/without_panels/' + image_paths[10]
print(path)
image = Image.open(path).convert('RGB')
image = image.resize(image_size)

draw = ImageDraw.Draw(image)
coordinates = [(56, 71),(100, 100)]
coordinates = AIUtil.invert_coordinates(coordinates, image_size)
draw.line(coordinates)
image

#%%
import pandas as pd
from PIL import Image, ImageDraw
from AIUtil import AIUtil

path_coordinates = 'data_coordinates.csv'
path = 'data/without_panels/'
data_coordinates = pd.read_csv(path_coordinates)
image_paths = os.listdir(path)
image_paths
data_coordinates

#%%
def input_coordinates(path):
    image = Image.open(path)
    x = input('input x coordinate:')
    y = input('input y coordinate:')
    return image

for image_path in image_paths:
    image_path = path + image_path
    if image_path in list(data_coordinates['address']):
        continue
    # input_coordinates(image_path)
    print(image_path)

#%%

path_image = 'data/without_panels/2304 E 50 S St, St. George, UT 84790.png'
image_size = (200,200)
def read_image(path, image_size = (200,200), mode = 'L'):
    image = Image.open(path_image)
    image = image.resize(image_size)
    image = image.convert('L')

    return image

def draw_point(image, coordinates):
    draw = ImageDraw.Draw(image)
    coordinates = AIUtil.invert_coordinates(coordinates, image_size)
    draw.line(coordinates)
    return draw
image = read_image(path_image)
coordinates = [(56, 71),(100, 100)]
image_new = draw_point(image, coordinates)
image_new

image

# %%
