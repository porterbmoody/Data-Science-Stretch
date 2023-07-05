#%%

from flask import Flask, render_template, request
from PanelFramework import PanelFramework
from RooftopImage import RooftopImage
from shapely.geometry import Polygon
import os
import pandas as pd
from termcolor import colored

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
