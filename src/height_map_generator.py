import random
from noise import pnoise2
import matplotlib.pyplot as plt

class HeightMapGenerator:

    def __init__(self, h_tiles, v_tiles):
        # corner-grid-dimensions:
        self.h_corners = h_tiles + 1
        self.v_corners = v_tiles + 1

        # init 2d array with -1 for debug purposes
        self.height_map = [[-1 for x in range(self.h_corners)] for y in range(self.v_corners)]

    def generate_heightmap():

        for v in range(self.v_corners):
            for h in range(self.h_corners):

                # calculate noise value
                noise_val = pnoise2(h*0.05,v*0.05, octaves = 1, persistence = 0.8, base = 42)
                # normalize to interall 0 - 1
                normalized_noise_val = (noise_val +1) * 0.5
                # transform noise value to height value
                height_value = transform_noise_to_height(normalized_noise_val)
                # add normalized value to height map
                self.height_map[v][h] = height_value

        werte = [val for row in self.height_map for val in row]  # flatten
        plt.hist(werte, bins=30)  # 30 Balken im Histogramm
        plt.title('Verteilung der Heightmap-Werte')
        plt.xlabel('Wert')
        plt.ylabel('Häufigkeit')
        plt.show()
        return Test

    def transform_noise_to_height(normalized_noise_value: float):
        if normalized_noise_value <= 0.45: return 0
        elif normalized_noise_value <= 0.48: return 1
        elif normalized_noise_value <= 0.55: return 2
        elif normalized_noise_value <= 0.65: return 3
        elif normalized_noise_value <= 0.75: return 4
        elif normalized_noise_value <= 1.0: return 5

    def flatten_jumps():
        pass