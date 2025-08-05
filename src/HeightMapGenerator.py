import random

# probabilities to change height depending on current height
UP_PROB = [0.2, 0.8, 0.8, 0.1, 0.3, 0.0]
DOWN_PROB = [0.0, 0.0, 0.1, 0.1, 0.2, 0.2]

def generate_heightmap(h_tiles: int, v_tiles: int, max_height: int = 5):

    # corner-grid-dimensions:
    h_corners = h_tiles + 1
    v_corners = v_tiles + 1

    # init 2d array with -1 for debug purposes
    H = [[-1 for x in range(h_corners)] for y in range(v_corners)]

    for v in range(v_corners):
        for h in range(h_corners):

            # collect neighbours to avoid jumps > 1
            neighbours = []

            if h > 0 and H[v][h-1] != -1:
                neighbours.append(H[v][h-1])
            if v > 0 and H[v-1][h] != -1:
                neighbours.append(H[v-1][h])

            if not neighbours:
                # no neighbour -> random height between 0 and max height
                value = 0
            else:
                # at least one neighbour -> determine current average height
                avg_height = sum(neighbours) / len(neighbours)
                value0 = round(avg_height)

                # make sure there are no jumps > 1
                lower = 0
                upper = max_height
                for n in neighbours:
                    lower = max(lower, n - 1)
                    upper = min(upper, n + 1)

                value1 = max(min(value0, upper), lower)

                down_prob = DOWN_PROB[min(value1, len(DOWN_PROB) - 1)]
                up_prob = UP_PROB[min(value1, len(UP_PROB) - 1)]

                value2 = value1
                r = random.random()
                if r < down_prob:
                    value2 -= 1
                elif r < down_prob + up_prob:
                    value2 += 1

                # check again for jumps > 1
                value3 = max(min(value2, upper), lower)
                value = value3

            H[v][h] = value

    return H


print(generate_heightmap(20,20, 5))