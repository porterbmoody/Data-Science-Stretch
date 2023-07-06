#%%
from RooftopImage import RooftopImage
from PanelFramework import PanelFramework
import os
from tkinter import *
from shapely.geometry import Polygon

addresses = os.listdir('cnn/images/images_without_panels')
addresses

address = '145 N Mall Dr UNIT 31, St. George, UT 84790'
# list_of_polygons = [
#   [
#   (315, 223),
#   (315, 418),
#   (410, 418),
#   (410, 223),
#   ],
#   [
#   (195, 225),
#   (195, 285),
#   (290, 285),
#   (240, 225),
#   ]
# ]

rooftop_image = RooftopImage(address)
rooftop_image.image_roof


#%%

address = '145 N Mall Dr UNIT 32, St. George, UT 84790'
list_of_polygons = [
  [
  (283, 208),
  (283, 400),
  (355, 400),
  (355, 208),
  ],
]

rooftop_image = RooftopImage(address)
rooftop_image.draw_roof_sections(list_of_polygons)
rooftop_image.draw_panels()
rooftop_image.image_roof

#%%

address = '145 N Mall Dr UNIT 34, St. George, UT 84790'
top, bottom, left, right = 400, 205, 310, 395
list_of_polygons = [
  [
  (400, 205),
  (310, 400),
  (395, 400),
  (395, 205),
  ],
]

rooftop_image = RooftopImage(address)
rooftop_image.draw_roof_sections(list_of_polygons)
rooftop_image.draw_panels()
rooftop_image.image_roof


#%%

address = '145 N Mall Dr UNIT 35, St. George, UT 84790'
list_of_polygons = [
  [
  (289, 205),
  (289, 400),
  (368, 400),
  (361, 205),
  ],
]

rooftop_image = RooftopImage(address)
rooftop_image.draw_roof_sections(list_of_polygons)
rooftop_image.draw_panels()
rooftop_image.image_roof

#%%
address = addresses[17]

list_of_polygons = [
  [
  (289, 205),
  (289, 400),
  (368, 400),
  (361, 205),
  ],
]

rooftop_image = RooftopImage(address)
# rooftop_image.draw_roof_sections(list_of_polygons)
# rooftop_image.draw_panels()
rooftop_image.image_roof


# %%
address = addresses[17]

list_of_polygons = [
  [
  (330, 210),
  (330, 408),
  (420, 408),
  (420, 210),
  ],
]

rooftop_image = RooftopImage(address)
rooftop_image.draw_roof_sections(list_of_polygons)
rooftop_image.draw_panels()
rooftop_image.image_roof

#%%
address = addresses[18]

list_of_polygons = [
  [
  (300, 210),
  (300, 408),
  (420, 408),
  (420, 210),
  ],
]

rooftop_image = RooftopImage(address)
rooftop_image.draw_roof_sections(list_of_polygons)
rooftop_image.draw_panels()
rooftop_image.image_roof
#%%
address = addresses[18]

list_of_polygons = [
  [
    (295, 207),
    (295, 399),
    (345, 400),
    (352, 370),
    (326, 342),
    (362, 310),
    (360, 207),
  ],
  [
    (225, 207),
    (260, 255),
    (226, 295),
    (230, 320),
    (260, 355),
    (225, 400),
    (295, 400),
    # (295, 355),
    # (295, 255),
    (295, 207),
  ],
]

rooftop_image = RooftopImage(address)
rooftop_image.draw_roof_sections(list_of_polygons)
rooftop_image.draw_panels()
rooftop_image.image_roof

# %%
address = addresses[19]

list_of_polygons = [
  [
  (225, 207),
  (260, 255),
  (226, 295),
  (230, 320),
  (260, 355),
  (295, 355),
  (295, 255),
  (295, 207),
  ],
  [
  (295, 207),
  (295, 405),
  (360, 405),
  (360, 207),
  ],
]

rooftop_image = RooftopImage(address)
rooftop_image.draw_roof_sections(list_of_polygons)
# rooftop_image.draw_panels()
rooftop_image.image_roof
# %%




