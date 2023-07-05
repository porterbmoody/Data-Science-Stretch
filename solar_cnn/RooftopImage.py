from PIL import Image, ImageDraw
import os
from termcolor import colored
import pandas as pd


class RooftopImage:
    """ Contains the data related to a single customer's rooftop image. Uses PIL's Image object as the rooftop image,
    and uses ImageDraw to draw coordinates contained in shapely's Polygon object
    """

    def __init__(self, address):
        # Remove .png extension if present
        if address.endswith('.png'):
            address = address[:-4]
            print(address)
        self.address = address
        # declare path variables
        self.path_base_image = 'static/images/'
        self.path_rooftop = self.path_base_image+'without_panels/'+address+'.png'
        self.path_rooftop_labeled = self.path_base_image+'with_panels/'+address+'.png'
        self.panel_frameworks = []

        if os.path.exists(self.path_rooftop_labeled):
            print('loading unlabeled roof', self.path_rooftop)
            print(colored('labeled address already exists: ' + address, 'red'))
            self.image_roof_labeled = Image.open(self.path_rooftop_labeled).convert("RGBA")
        else:
            print('address has not been labeled:', address)

        # all other variables
        self._load_rooftop_image()

    def _load_rooftop_image(self):
        print('loading rooftop image...', self.path_rooftop)
        self.image_roof = Image.open(self.path_rooftop).convert("RGBA")
        if self.image_roof.size[0] != 600:
            print(colored('resizing rooftop image', 'green'))
            self._rescale_rooftop_image(save = True)

    def add_panel_framework(self, panel_framework, draw_roof_sections=True ,draw_panels = True):
        self.panel_frameworks.append(panel_framework)
        if draw_roof_sections:
            self.draw_roof_sections()
        if draw_panels:
            self.draw_panels()

    def draw_roof_sections(self):
        if len(self.panel_frameworks) > 0:
            for panel_framework in self.panel_frameworks:
                self._draw_polygon(panel_framework.roof_section)

    def draw_panels(self):
        for panel_framework in self.panel_frameworks:
            [self._draw_polygon(panel) for panel in panel_framework.panels]

    def _draw_polygon(self, polygon):
        polygon_coordinates = polygon.exterior.coords
        # invert y coordinates
        inverted_polygon_coordinates = [(x, self.image_roof.size[1] - y) for x, y in polygon_coordinates]
        draw = ImageDraw.Draw(self.image_roof)
        draw.polygon(inverted_polygon_coordinates, outline = 'black', width = 1)
        # self.temp_save()

    def _rescale_rooftop_image(self, save=False):
        # new_size = (round(self.image_roof.size[0]*scale), round(self.image_roof.size[1]*scale))
        new_size = (600, 600)
        self.image_roof = self.image_roof.resize(new_size)
        if save:
            self.image_roof.save(self.path_rooftop)

    def temp_save(self):
        """Saves current image_rooftop PIL object to temporary path in 'temp' fodler
        """
        if len(self.panel_frameworks) > 0:
            print('saving with', len(self.panel_frameworks), 'panel frameworks')
            self.path_temp = self.path_base_image + 'temp/' + self.address + '.png'
            # print(self.path_temp)
            self.image_roof.save(self.path_temp)

    def save(self):
        if os.path.exists(self.path_rooftop_labeled):
            print('path already exists:', self.path_rooftop_labeled)
        else:
            self.image_roof.save(self.path_rooftop_labeled)

    def save_frameworks(self):
        """ Reads panel_frameworks.csv as current_data pandas dataframe.
        """
        # hmm... gonna have to get creative on this one
        self.path_panel_frameworks = self.path_base_image + 'panel_frameworks.csv'
        panel_framework_coordinates = [list(panel_framework.roof_section.exterior.coords) for panel_framework in self.panel_frameworks]
        print('saving panel coordinates:', panel_framework_coordinates)
        current_data = pd.read_csv(self.path_panel_frameworks)
        data_new = pd.DataFrame({
            'address' : self.address,
            'panel_framework' : panel_framework_coordinates,
        })
        data_new['panel_framework'] = data_new['panel_framework'].apply(lambda x: str(x))
        data_new = pd.concat([data_new, current_data]).drop_duplicates(keep='last')
        print('saving...')
        print(data_new)
        data_new.to_csv(self.path_panel_frameworks, index = False)


#%%

# import pandas as pd

# path = 'static/images/panel_frameworks.csv'
# current_data = pd.read_csv(path)



#%%



# %%

# data_to_save['panel_framework'] = data_to_save['panel_framework'].apply(lambda x: str(x))
# data_to_save

# # newline = ['119 N FIREROCK TRL, IVINS', '[[(242.0, 151.0), (186.0, 186.0), (244.0, 239.0), (291.0, 193.0), (311.0, 193.0), (354.0, 156.0), (242.0, 151.0)]]']
# # newline
# #%%

# data_to_save = pd.concat([data_to_save, current_data]).drop_duplicates(keep='last')
# data_to_save

# # current_data.merge(data_to_save, how = 'left')
# #%%
# import csv

# with open(path, 'a', newline='') as file:
#     writer = csv.writer()
#     # reader = csv.reader(file, delimiter=',')
#     # for row in reader:
#         # print(row)

