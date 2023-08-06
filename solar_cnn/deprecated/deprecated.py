
  # def _paste_panel_images(self) -> None:
    # for location in self.panel_layout.locations:
      # self._paste_panel(self.image_roof, self.panel_layout.image_panel, location)

  # def _paste_panel(self, panel, location):
    # vertices = (int(location[0]), int(self.image_roof.size[1] - location[1]))
    # rotation = location[2]
    # coordinates = (310, 600-/223-self.image_panel.size[1]+1)
    # if rotation != 0:
      # panel = panel.rotate(rotation, expand=True)
    # self.image_roof.paste(panel, vertices, panel)


# # locations format = [(x, y, rotational_angle)]
# base_x = 172
# base_y = 233
# locations = [
#   (base_x, base_y, 90),
#   (base_x, base_y + panel_layout.width, 90),
#   (base_x, base_y +panel_layout.width*2, 90),
#   (base_x, base_y +panel_layout.width*3, 90),
#   (base_x, base_y +panel_layout.width*4, 90),
#   (base_x, base_y +panel_layout.width*5, 90),
#   (base_x, base_y +panel_layout.width*6, 90),
#   (base_x, base_y +panel_layout.width*7, 90),
#   (base_x, base_y +panel_layout.width*8, 90),
#   (base_x, base_y +panel_layout.width*9, 90),
#   (base_x +panel_layout.height, base_y +panel_layout.width*0, 90),
#   (base_x +panel_layout.height, base_y +panel_layout.width*1, 90),
#   (base_x +panel_layout.height, base_y +panel_layout.width*2, 90),
#   (base_x +panel_layout.height, base_y +panel_layout.width*3, 90),
#   (base_x +panel_layout.height, base_y +panel_layout.width*4, 90),
#   (base_x +panel_layout.height, base_y +panel_layout.width*5, 90),
#   (base_x +panel_layout.height, base_y +panel_layout.width*6, 90),
#   (base_x +panel_layout.height, base_y +panel_layout.width*7, 90),
#   (base_x +panel_layout.height, base_y +panel_layout.width*8, 90),
#   (base_x +panel_layout.height, base_y +panel_layout.width*9, 90),
#   (base_x +panel_layout.height*2, base_y +panel_layout.width*0, 90),
#   (base_x +panel_layout.height*2, base_y +panel_layout.width*1, 90),
#   (base_x +panel_layout.height*2, base_y +panel_layout.width*2, 90),
#   (base_x +panel_layout.height*2, base_y +panel_layout.width*3, 90),
#   (base_x +panel_layout.height*2, base_y +panel_layout.width*4, 90),
#   (base_x +panel_layout.height*2, base_y +panel_layout.width*5, 90),
#   (base_x +panel_layout.height*2, base_y +panel_layout.width*6, 90),
#   (base_x +panel_layout.height*2, base_y +panel_layout.width*8, 90),
#   (base_x +panel_layout.height*2, base_y +panel_layout.width*9, 90),
#   (base_x +panel_layout.height*3, base_y +panel_layout.width*0, 90),
#   (base_x +panel_layout.height*3, base_y +panel_layout.width*1, 90),
#   (base_x +panel_layout.height*3, base_y +panel_layout.width*2, 90),
#   (base_x +panel_layout.height*3, base_y +panel_layout.width*3, 90),
#   (base_x +panel_layout.height*3, base_y +panel_layout.width*4, 90),
#   (base_x +panel_layout.height*3, base_y +panel_layout.width*5, 90),
#   (base_x +panel_layout.height*3, base_y +panel_layout.width*6, 90),
#   (base_x +panel_layout.height*3, base_y +panel_layout.width*7, 90),
#   (base_x +panel_layout.height*3, base_y +panel_layout.width*8, 90),
#   (base_x +panel_layout.height*3, base_y +panel_layout.width*9, 90),
#   (base_x +panel_layout.height*4, base_y +panel_layout.width*0, 90),
#   (base_x +panel_layout.height*4, base_y +panel_layout.width*1, 90),
#   (base_x +panel_layout.height*4, base_y +panel_layout.width*2, 90),
#   (base_x +panel_layout.height*4, base_y +panel_layout.width*3, 90),
#   (base_x +panel_layout.height*4, base_y +panel_layout.width*4, 90),
#   (base_x +panel_layout.height*4, base_y +panel_layout.width*5, 90),
#   (base_x +panel_layout.height*4, base_y +panel_layout.width*6, 90),
#   (base_x +panel_layout.height*4, base_y +panel_layout.width*7, 90),
#   (base_x +panel_layout.height*4, base_y +panel_layout.width*8, 90),
#   (base_x +panel_layout.height*4, base_y +panel_layout.width*9, 90),
#   (base_x + 72 +panel_layout.height*0, base_y-6, 90),
#   (base_x + 72 +panel_layout.height*1, base_y-6, 90),
#   (base_x + 72 +panel_layout.height*2, base_y-6, 90),
#   (base_x + 72 +panel_layout.height*3, base_y-6, 90),
#   (base_x + 72 +panel_layout.height*0, base_y-6+panel_layout.width, 90),
#   (base_x + 72 +panel_layout.height*1, base_y-6+panel_layout.width, 90),
#   (base_x + 72 +panel_layout.height*2, base_y-6+panel_layout.width, 90),
#   (base_x + 72 +panel_layout.height*3, base_y-6+panel_layout.width, 90),
#   (base_x+76, base_y+37+panel_layout.width*0, 90),
#   (base_x+76, base_y+37 +panel_layout.width*1, 90),
#   (base_x+76, base_y+37 +panel_layout.width*2, 90),
#   (base_x+76, base_y+37 +panel_layout.width*3, 90),
#   (base_x+76, base_y+37 +panel_layout.width*4, 90),
#   (base_x+76 +panel_layout.height, base_y+37 +panel_layout.width*0, 90),
#   (base_x+76 +panel_layout.height, base_y+37 +panel_layout.width*1, 90),
#   (base_x+76 +panel_layout.height, base_y+37 +panel_layout.width*2, 90),
#   (base_x+76 +panel_layout.height, base_y+37 +panel_layout.width*3, 90),
#   (base_x+76 +panel_layout.height, base_y+37 +panel_layout.width*4, 90),
#   (base_x+76 +panel_layout.height, base_y+37 +panel_layout.width*5, 90),
#   (base_x+76 +panel_layout.height*2, base_y+37 +panel_layout.width*2, 90),
#   (base_x+76 +panel_layout.height*2, base_y+37 +panel_layout.width*3, 90),
#   (base_x+76 +panel_layout.height*2, base_y+37 +panel_layout.width*4, 90),
#   (base_x+76 +panel_layout.height*3, base_y+37 +panel_layout.width*2.5, 90),
#   (base_x+76 +panel_layout.height*3, base_y+37 +panel_layout.width*3.5, 90),
#   (base_x+76 +panel_layout.height*4, base_y+37 +panel_layout.width*3, 90),
#   (base_x+151+panel_layout.width*0, base_y+103, 0),
#   (base_x+151+panel_layout.width*1, base_y+103, 0),
#   (base_x+151-panel_layout.width, base_y+103+panel_layout.height, 0),
#   (base_x+151+panel_layout.width*0, base_y+103+panel_layout.height, 0),
#   (base_x+151+panel_layout.width*1, base_y+103+panel_layout.height, 0),
# ]
# panel_layout.add_locations(locations)
# rooftop_image.add_panel_layout(panel_layout)
# rooftop_image.image_roof

# #%%

# address = '145 N Mall Dr UNIT 24, St. George, UT 84790'
# rooftop_image = RooftopImage(address = address)
# panel_layout = PanelLayout()

# base_x = 191
# base_y = 240
# locations = [
#   (base_x, base_y, 0),
#   (base_x + panel_layout.width, base_y, 0),
#   (base_x + panel_layout.width*2, base_y, 0),
#   (base_x + panel_layout.width*3, base_y, 0),
#   (base_x + panel_layout.width*4, base_y, 0),
#   (base_x + panel_layout.width*5, base_y, 0),
#   (base_x + panel_layout.width*6, base_y, 0),
#   (base_x + panel_layout.width*7, base_y, 0),
#   (base_x + panel_layout.width*8, base_y, 0),
#   (base_x + panel_layout.width*9, base_y, 0),
#   (base_x+panel_layout.width*.5, base_y +panel_layout.height, 0),
#   (base_x+panel_layout.width*1.5, base_y +panel_layout.height, 0),
#   (base_x+panel_layout.width*2.5, base_y +panel_layout.height, 0),
#   (base_x + panel_layout.width*3.5, base_y +panel_layout.height, 0),
#   (base_x + panel_layout.width*4.5, base_y +panel_layout.height, 0),
#   (base_x + panel_layout.width*5.5, base_y +panel_layout.height, 0),
#   (base_x + panel_layout.width*6.5, base_y +panel_layout.height, 0),
#   (base_x + panel_layout.width*7.5, base_y +panel_layout.height, 0),
#   (base_x + panel_layout.width*8.5, base_y +panel_layout.height, 0),
#   (base_x + panel_layout.width, base_y+panel_layout.height*2, 0),
#   (base_x + panel_layout.width*2, base_y+panel_layout.height*2, 0),
#   (base_x + panel_layout.width*3, base_y+panel_layout.height*2, 0),
#   (base_x + panel_layout.width*2, base_y+panel_layout.height*3, 0),
#   (base_x-25, base_y+37 - panel_layout.width*1, 90),
#   (base_x-25, base_y+37 + panel_layout.width*0, 90),
#   (base_x-25, base_y+37 + panel_layout.width*1, 90),
#   (base_x-25, base_y+37 + panel_layout.width*2, 90),
#   (base_x-25, base_y+37 + panel_layout.width*3, 90),
#   (base_x-25, base_y+37 + panel_layout.width*4, 90),
#   (base_x-25, base_y+37 + panel_layout.width*5, 90),
#   (base_x-25, base_y+37 + panel_layout.width*6, 90),
#   (base_x-25, base_y+37 + panel_layout.width*7, 90),
#   (base_x-25 + panel_layout.height, base_y+37, 90),
#   (base_x-25 + panel_layout.height, base_y+37 + panel_layout.width, 90),
#   (base_x-25 + panel_layout.height, base_y+37 + panel_layout.width*2, 90),
#   (base_x-25 + panel_layout.height, base_y+37 + panel_layout.width*3, 90),
#   (base_x-25 + panel_layout.height, base_y+37 + panel_layout.width*4, 90),
#   (base_x-25 + panel_layout.height, base_y+37 + panel_layout.width*5, 90),
#   (base_x-25 + panel_layout.height, base_y+37 + panel_layout.width*6, 90),
#   (base_x-25 + panel_layout.height*2, base_y+37 + panel_layout.width, 90),
#   (base_x-25 + panel_layout.height*2, base_y+37 + panel_layout.width*2, 90),
#   (base_x-25 + panel_layout.height*2, base_y+37 + panel_layout.width*3, 90),
#   (base_x-25 + panel_layout.height*2, base_y+37 + panel_layout.width*4, 90),
#   (base_x-25 + panel_layout.height*2, base_y+37 + panel_layout.width*5, 90),
#   (base_x-25 + panel_layout.height*3, base_y+37 + panel_layout.width*1.5, 90),
#   (base_x-25 + panel_layout.height*3, base_y+37 + panel_layout.width*2.5, 90),
#   (base_x-25 + panel_layout.height*3, base_y+37 + panel_layout.width*3.5, 90),
#   (base_x+48, base_y+60 + panel_layout.width, 90),
#   (base_x+48, base_y+60 + panel_layout.width*2, 90),
#   (base_x+48+panel_layout.height, base_y+60 + panel_layout.width*2, 90),
#   (base_x+48+panel_layout.height, base_y+60 + panel_layout.width, 90),
#   (base_x+48+panel_layout.height, base_y+60 + panel_layout.width*3, 90),
#   (base_x+48, base_y+60 + panel_layout.width*1, 90),
#   (base_x+48, base_y+60 + panel_layout.width*2, 90),
# ]
# panel_layout.add_locations(locations)
# rooftop_image.add_panel_layout(panel_layout)
# rooftop_image.image_roof


# #%%
# address = '145 N Mall Dr UNIT 25, St. George, UT 84790'
# rooftop_image = RooftopImage(address = address)
# panel_layout = PanelLayout()

# base_x = 141
# base_y = 290
# locations = [
#   (base_x, base_y, 90),
#   (base_x, base_y+panel_layout.width, 90),
#   (base_x, base_y+panel_layout.width*2, 90),
#   (base_x, base_y+panel_layout.width*3, 90),
#   (base_x, base_y+panel_layout.width*4, 90),
#   (base_x+panel_layout.height, base_y+panel_layout.width*1, 90),
#   (base_x+panel_layout.height, base_y+panel_layout.width*2, 90),
#   (base_x+panel_layout.height, base_y+panel_layout.width*3, 90),
#   (base_x+panel_layout.height*2, base_y+panel_layout.width*2, 90),
#   (base_x+65, base_y-72, 0),
#   (base_x+65+panel_layout.width, base_y-72, 0),
#   (base_x+65+panel_layout.width*2, base_y-72, 0),
#   (base_x+65+panel_layout.width*3, base_y-72, 0),
#   (base_x+65+panel_layout.width*4, base_y-72, 0),
#   (base_x+65+panel_layout.width*5, base_y-72, 0),
#   (base_x+65+panel_layout.width*6, base_y-72, 0),
#   (base_x+65+panel_layout.width*7, base_y-72, 0),
#   (base_x+65+panel_layout.width*1, base_y-72+panel_layout.height, 0),
#   (base_x+65+panel_layout.width*2, base_y-72+panel_layout.height, 0),
#   (base_x+65+panel_layout.width*3, base_y-72+panel_layout.height, 0),
#   (base_x+65+panel_layout.width*4, base_y-72+panel_layout.height, 0),
#   (base_x+65+panel_layout.width*5, base_y-72+panel_layout.height, 0),
#   (base_x+65+panel_layout.width*6, base_y-72+panel_layout.height, 0),
#   (base_x+65+panel_layout.width*7, base_y-72+panel_layout.height, 0),
#   (base_x+65+panel_layout.width*1, base_y-72+panel_layout.height*2, 0),
#   (base_x+65+panel_layout.width*2, base_y-72+panel_layout.height*2, 0),
#   (base_x+65+panel_layout.width*3, base_y-72+panel_layout.height*2, 0),
#   (base_x+65+panel_layout.width*2, base_y-72+panel_layout.height*3, 0),
#   (base_x+65+panel_layout.width*2, base_y-72+panel_layout.height*3, 0),
#   (base_x+168, base_y+31, 0),
#   (base_x+168+panel_layout.width, base_y+31, 0),
#   (base_x+168+panel_layout.width*2, base_y+31, 0),
#   (base_x+158+panel_layout.width*0, base_y+31+panel_layout.height, 0),
#   (base_x+158+panel_layout.width*1, base_y+31+panel_layout.height, 0),
#   (base_x+158+panel_layout.width*2, base_y+31+panel_layout.height, 0),
#   (base_x+158+panel_layout.width*2, base_y+31+panel_layout.height, 0),
#   (base_x+158+panel_layout.width*0, base_y+31+panel_layout.height*2, 0),
#   (base_x+158+panel_layout.width*1, base_y+31+panel_layout.height*2, 0),
#   (base_x+158+panel_layout.width*2, base_y+31+panel_layout.height*2, 0),
# ]
# panel_layout.add_locations(locations)
# rooftop_image.add_panel_layout(panel_layout)
# rooftop_image.image_roof


# # %%
# address = '145 N Mall Dr UNIT 26, St. George, UT 84790'
# rooftop_image = RooftopImage(address = address)
# panel_layout = PanelLayout()

# base_x = 165
# base_y = 224
# locations = [
#   (base_x,base_y,0),
#   (base_x+panel_layout.width,base_y,0),
#   (base_x+panel_layout.width*0,base_y+panel_layout.height*1,0),
#   (base_x+panel_layout.width*1,base_y+panel_layout.height*1,0),
#   (base_x+panel_layout.width*0,base_y+panel_layout.height*2,0),
#   (base_x+panel_layout.width*1,base_y+panel_layout.height*2,0),
#   (base_x+panel_layout.width*2,base_y+panel_layout.height*2,0),
#   (base_x+panel_layout.width*0,base_y+panel_layout.height*3,0),
#   (base_x+panel_layout.width*1,base_y+panel_layout.height*3,0),
#   (base_x+panel_layout.width*2,base_y+panel_layout.height*3,0),
#   (base_x+panel_layout.width*3,base_y+panel_layout.height*3,0),
#   (base_x+102,base_y+4+panel_layout.width*0,90),
#   (base_x+102,base_y+4+panel_layout.width*1,90),
#   (base_x+102,base_y+4+panel_layout.width*2,90),
#   (base_x+102,base_y+4+panel_layout.width*3,90),
#   (base_x+102,base_y+4+panel_layout.width*4,90),
#   (base_x+102,base_y+4+panel_layout.width*5,90),
#   (base_x+102,base_y+4+panel_layout.width*6,90),
#   (base_x+102,base_y+4+panel_layout.width*7,90),
#   (base_x+102+panel_layout.height*1,base_y+4+panel_layout.width*0,90),
#   (base_x+102+panel_layout.height*2,base_y+4+panel_layout.width*0,90),
#   (base_x+102+panel_layout.height*1,base_y+4+panel_layout.width*1,90),
#   (base_x+102+panel_layout.height*2,base_y+4+panel_layout.width*1,90),
#   (base_x+102+panel_layout.height*1,base_y+4+panel_layout.width*2,90),
#   (base_x+102+panel_layout.height*2,base_y+4+panel_layout.width*2,90),
#   (base_x+102+panel_layout.height*1,base_y+4+panel_layout.width*3,90),
#   (base_x+102+panel_layout.height*2,base_y+4+panel_layout.width*3,90),
#   (base_x+102+panel_layout.height*1,base_y+4+panel_layout.width*4,90),
#   (base_x+102+panel_layout.height*2,base_y+4+panel_layout.width*4,90),
#   (base_x+102+panel_layout.height*1,base_y+4+panel_layout.width*5,90),
#   (base_x+102+panel_layout.height*2,base_y+4+panel_layout.width*5,90),
#   (base_x+102+panel_layout.height*1,base_y+4+panel_layout.width*6,90),
#   (base_x+102+panel_layout.height*2,base_y+4+panel_layout.width*6,90),
#   (base_x+102+panel_layout.height*1,base_y+4+panel_layout.width*7,90),
#   # (base_x+102+panel_layout.height*2,base_y+4+panel_layout.width*7,90),
#   (base_x+102+panel_layout.height*3,base_y+4+panel_layout.width*1,90),
#   (base_x+102+panel_layout.height*3,base_y+4+panel_layout.width*2,90),
#   (base_x+102+panel_layout.height*3,base_y+4+panel_layout.width*3,90),
#   (base_x+102+panel_layout.height*3, base_y+4+panel_layout.width*3, 90),
#   (base_x+102+panel_layout.height*4, base_y+4+panel_layout.width*2.5, 90),
#   (base_x+102+panel_layout.height*4, base_y+4+panel_layout.width*1.5, 90),
#   (base_x+102+panel_layout.height*4, base_y+4+panel_layout.width*1.5, 90),
#   (base_x+191, base_y+126, 90),
#   (base_x+191, base_y+126+panel_layout.width, 90),
#   (base_x+191, base_y+126+panel_layout.width*2, 90),
#   (base_x+191-panel_layout.height, base_y+126+panel_layout.width*.5, 90),
#   (base_x+191-panel_layout.height, base_y+126+panel_layout.width*.5, 90),
#   (base_x+191-panel_layout.height, base_y+126+panel_layout.width*1.5, 90),
#   (base_x+191-panel_layout.height*2, base_y+126+panel_layout.width*1, 90),
# ]
# panel_layout.add_locations(locations)
# rooftop_image.add_panel_layout(panel_layout)
# rooftop_image.image_roof


# # %%

# base_x = 188
# base_y = 238
# locations = [
#   (base_x,base_y,0),
#   (base_x+panel_layout.width,base_y,0),
#   (base_x+panel_layout.width*0,base_y+panel_layout.height,0),
#   (base_x+panel_layout.width*1,base_y+panel_layout.height,0),
#   (base_x+panel_layout.width*2,base_y+panel_layout.height,0),
#   (base_x+panel_layout.width*1,base_y+panel_layout.height*2,0),
#   (base_x+panel_layout.width*2,base_y+panel_layout.height*2,0),
#   (base_x+panel_layout.width*3,base_y+panel_layout.height*2,0),
#   (base_x+panel_layout.width*1,base_y+panel_layout.height*3,0),
#   (base_x+panel_layout.width*2,base_y+panel_layout.height*3,0),
#   (base_x+132+panel_layout.height*0,base_y+6,90),
#   (base_x+132+panel_layout.height*1,base_y+6,90),
#   (base_x+132+panel_layout.height*2,base_y+6,90),
#   (base_x+132+panel_layout.height*3,base_y+6,90),
#   (base_x+132+panel_layout.height*4,base_y+6,90),
#   (base_x+132+panel_layout.height*5,base_y+6,90),
#   (base_x+132+panel_layout.height*0,base_y+panel_layout.width*1+6,90),
#   (base_x+132+panel_layout.height*1,base_y+panel_layout.width*1+6,90),
#   (base_x+132+panel_layout.height*2,base_y+panel_layout.width*1+6,90),
#   (base_x+132+panel_layout.height*3,base_y+panel_layout.width*1+6,90),
#   (base_x+132+panel_layout.height*4,base_y+panel_layout.width*1+6,90),
#   (base_x+132+panel_layout.height*5,base_y+panel_layout.width*1+6,90),
#   (base_x+132+panel_layout.height*0,base_y+panel_layout.width*2+6,90),
#   (base_x+132+panel_layout.height*1,base_y+panel_layout.width*2+6,90),
#   (base_x+132+panel_layout.height*2,base_y+panel_layout.width*2+6,90),
#   (base_x+132+panel_layout.height*3,base_y+panel_layout.width*2+6,90),
#   (base_x+132+panel_layout.height*4,base_y+panel_layout.width*2+6,90),
#   (base_x+132+panel_layout.height*5,base_y+panel_layout.width*2+6,90),
#   (base_x+132+panel_layout.height*0,base_y+panel_layout.width*3+6,90),
#   # (base_x+132+panel_layout.height*1,base_y+panel_layout.width*3+6,90),
#   (base_x+132+panel_layout.height*2,base_y+panel_layout.width*3+6,90),
#   (base_x+132+panel_layout.height*3,base_y+panel_layout.width*3+6,90),
#   (base_x+132+panel_layout.height*4,base_y+panel_layout.width*3+6,90),
#   (base_x+132+panel_layout.height*5,base_y+panel_layout.width*3+6,90),
#   (base_x+132+panel_layout.height*0,base_y+panel_layout.width*4+6,90),
#   (base_x+132+panel_layout.height*1,base_y+panel_layout.width*4+6,90),
#   (base_x+132+panel_layout.height*1,base_y+panel_layout.width*4+6,90),
# ]
# # panel_layout.add_locations(locations)
# # rooftop_image.add_panel_layout(panel_layout)

# #%%
#%%
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
x = np.array([1,2,3,4, 5, 6, 7])
y = 2*x
ax.plot(x, y)
plt.show()

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




