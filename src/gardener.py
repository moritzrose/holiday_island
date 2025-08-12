# i could have implemented this logic into the tile class, but I wanted a gardener, cause I wanted one
import random
from src.asset_manager import load_plants
from src.world_configuration import Config

class Gardener:

    def __init__(self):
        self.plants = load_plants()

    def grow_plants(self, tile_id):
        number = random.random()
        if tile_id != "0000" or number > Config.PLANT_PROB:
            return None
        # give every plant the same probability depending on the general vegetation probability
        even_divider = 1 / len(self.plants) * Config.PLANT_PROB

        if number <= even_divider * 1:
            return self.plants.get("bush")
        elif number <= even_divider * 2:
            return self.plants.get("palm1")
        elif number <= even_divider * 3:
            return self.plants.get("palm2")
        elif number <= even_divider * 4:
            return self.plants.get("palm3")
        elif number <= even_divider * 5:
            return self.plants.get("palm4")
        elif number <= even_divider * 6:
            return self.plants.get("palm5")
        elif number <= even_divider * 7:
            return self.plants.get("palm6")
        elif number <= even_divider * 8:
            return self.plants.get("palm7")
        elif number <= even_divider * 9:
            return self.plants.get("palm8")
        else:
            return self.plants.get("palm9")

