from shapely.geometry import Point, Polygon
from PIL import Image


class PanelFramework:
    """
    Contains all the data related to the rooftop section bounding polygons and the rectangles held inside.
    shapely Polygons are used much here.
    """

    def __init__(self, roof_section: Polygon) -> None:
        self.path_panel = 'static/images/panel_swag.png'
        self._load_panel_image()
        self.roof_section = roof_section
        self._calculate_panels()

    def _load_panel_image(self):
        print('reading panel', self.path_panel)
        self.image_panel = Image.open(self.path_panel).convert("RGBA")
        self.panel_width = self.image_panel.size[0]
        self.panel_height = self.image_panel.size[1]

    def _calculate_panels(self):
        self.panels = []
        # get lower left point to start
        base_x, base_y = self.roof_section.exterior.coords[0]
        # right side
        for column_num in range(20):
            for height_num in range(20):
                self._create_panel(base_x+5, base_y+5)
                self.shift_panel(self.panel_width*column_num, self.panel_height*height_num)
                # check if panel is within rooftop polygon bounds
                if self.is_valid():
                    self.panels.append(self.current_panel)

                # left side
                self._create_panel(base_x - self.panel_width + 5, base_y + 5)
                self.shift_panel(-self.panel_width * column_num, self.panel_height * height_num)
                # check if panel is within rooftop polygon bounds
                if self.is_valid():
                    self.panels.append(self.current_panel)

    def _create_panel(self, x, y):
        panel_coordinates = [
            (x, y),
            (x, y + self.panel_height),
            (x + self.panel_width, y + self.panel_height),
            (x + self.panel_width, y),
            ]
        self.current_panel = Polygon(panel_coordinates)

    def add_panel_framework(self, polygon_roof_section):
        self.polygon_roof_section = polygon_roof_section

    def is_valid(self):
        valid_coordinates = [self.roof_section.contains(Point(x, y)) for x, y in self.current_panel.exterior.coords]
        return all(valid_coordinates)

    def shift_panel(self, x_distance, y_distance):
        new_coords = [(x + x_distance, y + y_distance) for x, y in self.current_panel.exterior.coords]
        self.current_panel = Polygon(new_coords)
