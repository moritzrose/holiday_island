# i could have implemented this logic into the tile class, but I wanted a gardener
import random
from src.asset_manager import load_plants
from src.world_configuration import Config

class Gardener:

    def __init__(self):
        self.plants = load_plants()
        self.greenhouse = dict()

    def grow_plants(self, tile_id, grid_x, grid_y):
        number = random.random()

        # if the terrain is not suitable or the random number too high, do not plant anything
        if tile_id != "0000" or number > Config.PLANT_PROB:
            return None

        # give every plant the same probability depending on the general vegetation probability
        even_divider = 1 / len(self.plants) * Config.PLANT_PROB
        plant = None

        if number <= even_divider * 1:
            plant = "palm1"
        elif number <= even_divider * 2:
            plant = "palm2"
        elif number <= even_divider * 3:
            plant = "palm3"
        elif number <= even_divider * 4:
            plant = "palm4"
        elif number <= even_divider * 5:
            plant = "palm5"
        elif number <= even_divider * 6:
            plant = "palm6"
        elif number <= even_divider * 7:
            plant = "palm7"
        elif number <= even_divider * 8:
            plant = "palm8"
        elif number <= even_divider * 9:
            plant = "palm9"
        else:
            plant = "bush"

        # add plant and coordinates to the greenhouse to keep track "grid_x, grid_y" : "bush
        self.greenhouse[f"{grid_x},{grid_y}"] = plant
        return self.plants.get(plant)
