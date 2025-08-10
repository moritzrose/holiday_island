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

    def generate_heightmap(self):

        for v in range(self.v_corners):
            for h in range(self.h_corners):

                # calculate noise value
                noise_val = pnoise2(h*0.05,v*0.05, octaves = 2, persistence = 0.8, base = 42)
                # normalize to interall 0 - 1
                normalized_noise_val = (noise_val +1) * 0.5
                # transform noise value to height value
                height_value = self.transform_noise_to_height(normalized_noise_val)
                # add normalized value to height map
                self.height_map[v][h] = height_value

        self.flatten_jumps()

        werte = [val for row in self.height_map for val in row]  # flatten
        plt.hist(werte, bins=30)  # 30 Balken im Histogramm
        plt.title('Verteilung der Heightmap-Werte')
        plt.xlabel('Wert')
        plt.ylabel('Häufigkeit')
        plt.show()
        return self.height_map

    def transform_noise_to_height(self, normalized_noise_value: float):
        if normalized_noise_value <= 0.5: return 0
        elif normalized_noise_value <= 0.53: return 1
        elif normalized_noise_value <= 0.56: return 2
        elif normalized_noise_value <= 0.61: return 3
        elif normalized_noise_value <= 0.66: return 4
        elif normalized_noise_value <= 0.7: return 5
        elif normalized_noise_value <= 1.0: return 6

    # flattens height jumps > 1
    def flatten_jumps(self):

        for v in range(self.v_corners):
            for h in range(self.h_corners):

                height = self.height_map[v][h]
                min_height = height - 1
                max_height = min_height + 1

                h_neighbour = self.height_map[v][h+1]
                v_neighbour = self.height_map[v+1][h]
                if h_neighbour > max_height or h_neighbour < min_height:
                    clamp(self.height_map[v+1][h],min_height, max_height)

                if v_neighbour > max_height or v_neighbour < min_height:
                    clamp(self.height_map[v+1][h],min_height, max_height)