# i could have implemented this logic into the tile class, but I wanted a gardener, cause I wanted one
import random
import pygame





class Gardener:

    @staticmethod
    def load_plants():
        # plants
        plants = {
            "bush": {"sprite": pygame.image.load("../resources/plants/bush.png").convert_alpha()},
            "palm1": {"sprite": pygame.image.load("../resources/plants/palm1.png").convert_alpha()},
            "palm2": {"sprite": pygame.image.load("../resources/plants/palm2.png").convert_alpha()},
            "palm3": {"sprite": pygame.image.load("../resources/plants/palm3.png").convert_alpha()},
            "palm4": {"sprite": pygame.image.load("../resources/plants/palm4.png").convert_alpha()},
            "palm5": {"sprite": pygame.image.load("../resources/plants/palm5.png").convert_alpha()},
            "palm6": {"sprite": pygame.image.load("../resources/plants/palm6.png").convert_alpha()},
            "palm7": {"sprite": pygame.image.load("../resources/plants/palm7.png").convert_alpha()},
            "palm8": {"sprite": pygame.image.load("../resources/plants/palm8.png").convert_alpha()},
            "palm9": {"sprite": pygame.image.load("../resources/plants/palm9.png").convert_alpha()},
        }
        return plants

    def grow_plants(self, tile_id):
        number = random.random()
        if tile_id != "0000" or number <= 0.8:
            return None
        elif number <= 0.82:
            return self.plants.get("bush")
        elif number <= 0.84:
            return self.plants.get("palm1")
        elif number <= 0.86:
            return self.plants.get("palm2")
        elif number <= 0.88:
            return self.plants.get("palm3")
        elif number <= 0.9:
            return self.plants.get("palm4")
        elif number <= 0.92:
            return self.plants.get("palm5")
        elif number <= 0.94:
            return self.plants.get("palm6")
        elif number <= 0.96:
            return self.plants.get("palm7")
        elif number <= 0.98:
            return self.plants.get("palm8")
        else:
            return self.plants.get("palm9")

    def __init__(self):
        self.plants = self.load_plants()
