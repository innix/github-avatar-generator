'''
Generates GitHub-esque avatar images.
'''

from wand.image import Image
from wand.color import Color
import random

def generate(size, block_size, block_count, color=None, block_color=None):
    if color is None:
        color = '#f0f0f0'

    block_color = Color(block_color
                        if block_color is not None
                        else 'rgb' + str(_random_color()))

    # Create canvas.
    img = Image(width=size, height=size, background=Color(color))

    # Create matrix.
    matrix_size = (size / block_size) - 1
    matrix = [[0 for x in range(matrix_size)] for x in range(matrix_size)]

    # Plot points.
    plotted = 0
    while plotted < block_count:
        x = random.randrange(0, matrix_size)
        y = random.randrange(0, matrix_size)

        # If a point has already been plotted at this point.
        if matrix[x][y]:
            continue

        # If the generated x-axis is in the centre.
        central = (x == (matrix_size / 2))

        # Plot point.
        matrix[x][y] = True
        plotted += 1

        # If not a central point, plot a symmetrical point.
        if not central:
            matrix[matrix_size - x - 1][y] = True
            plotted += 1

    # Draw the plotted points on the image.
    for x in range(0, matrix_size):
        for y in range(0, matrix_size):
            if not matrix[x][y]:
                continue

            block_x = ((x + 1) * block_size) - (block_size / 2)
            block_y = ((y + 1) * block_size) - (block_size / 2)

            # Draws the rectangle.
            with Image(width=block_size,
                       height=block_size,
                       background=block_color) as rect:
                img.composite(image=rect, left=block_x, top=block_y)

    return img

def _random_color():
    palette_presets = [
        (225, 30, 30), # red
        (30, 225, 30), # green
        (30, 30, 225), # blue
        (190, 60, 210), # magenta
        (220, 220, 90), # yellow
        (210, 120, 110), # brick red
        (150, 220, 225) # turquoise
    ]

    r, g, b = palette_presets[random.randrange(0, len(palette_presets))]

    variation = 30
    r = min(255, max(0, r + random.randint(-variation, variation)))
    g = min(255, max(0, g + random.randint(-variation, variation)))
    b = min(255, max(0, b + random.randint(-variation, variation)))

    return (r, g, b)
