from noise import pnoise2
import matplotlib.pyplot as plt

from src.game_configuration import WORLD_SEED, SHOW_HEIGHT_DISTRIBUTION


def transform_noise_to_height(normalized_noise_value: float):
    if normalized_noise_value <= 0.51:
        return 0
    elif normalized_noise_value <= 0.53:
        return 1
    elif normalized_noise_value <= 0.55:
        return 2
    elif normalized_noise_value <= 0.6:
        return 3
    elif normalized_noise_value <= 0.63:
        return 4
    elif normalized_noise_value <= 0.75:
        return 5
    else:
        return 6


def clamp(value, min_value, max_value):
    if value < min_value:
        return min_value
    elif value > max_value:
        return max_value
    else:
        return value


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
                noise_val = pnoise2(h * 0.03, v * 0.03, octaves=15, persistence=0.4, base=WORLD_SEED)

                # normalize noise value to interval 0 - 1
                normalized_noise_val = (noise_val + 1) * 0.5

                # transform noise value to height value
                height_value = transform_noise_to_height(normalized_noise_val)

                # add height value to height map
                self.height_map[v][h] = height_value

        self.flatten_jumps()

        if SHOW_HEIGHT_DISTRIBUTION:
            self.show_height_distribution()

        return self.height_map

    # flattens height jumps > 1
    def flatten_jumps(self):

        for v in range(self.v_corners):
            for h in range(self.h_corners):

                height = self.height_map[v][h]
                min_height = max(height - 1, 0)
                max_height = min(height + 1, 6)

                if v < self.v_corners - 1:
                    v_neighbour = self.height_map[v + 1][h]
                    if v_neighbour > max_height or v_neighbour < min_height:
                        v_neighbour = clamp(v_neighbour, min_height, max_height)
                        self.height_map[v + 1][h] = v_neighbour
                if h < self.v_corners - 1:
                    h_neighbour = self.height_map[v][h + 1]
                    if h_neighbour > max_height or h_neighbour < min_height:
                        h_neighbour = clamp(h_neighbour, min_height, max_height)
                        self.height_map[v][h + 1] = h_neighbour

    # helper method to show height distribution statistic
    def show_height_distribution(self):
        werte = [val for row in self.height_map for val in row]  # flatten
        plt.hist(werte, bins=30)  # 30 Balken im Histogramm
        plt.title('Verteilung der Heightmap-Werte')
        plt.xlabel('Wert')
        plt.ylabel('Häufigkeit')
        plt.show()
