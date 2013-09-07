'''
Generates GitHub-esque avatar images.

Usage:
    avatar-gen.py <canvas_size> <pixel_count> <pixel_colour> <out_file>

    canvas_size - The size (width and height) of the image in pixels.
    pixel_count - The number of (enlarged) pixels to use in the image.
    pixel_colour - The colour of the pixels.
    out_file - The output file path.

Example:
    avatar-gen.py 420 12 "#a30000" test.png
'''
from wand.image import Image
from wand.color import Color
import numpy as np
import sys
import random

def generate(canvasSize, pixelSize, pixelCount, pixelColour, bgColour):
    img = Image(width=canvasSize, height=canvasSize, background=bgColour)
    img.format = 'png'

    # Create matrix.
    matrixSize = (canvasSize / pixelSize) - 1
    matrix = np.zeros((matrixSize, matrixSize), dtype=bool)

    # Plot points.
    plotted = 0
    while plotted < pixelCount:
        x = random.randrange(0, matrixSize)
        y = random.randrange(0, matrixSize)

        # If a point has already been plotted at this point.
        if matrix[x, y]:
            continue

        # If the generated x-axis is in the centre.
        central = (x == (matrixSize / 2))

        # Plot point.
        matrix[x, y] = True
        plotted += 1

        # If not a central point, plot a symmetrical point.
        if not central:
            matrix[matrixSize - x - 1, y] = True
            plotted += 1

    # Offset.
    posOffset = -(pixelSize / 2)

    # Draw the plotted points on to the image.
    for x in range(0, matrixSize):
        for y in range(0, matrixSize):
            if matrix[x, y]:
                pixelX = ((x + 1) * pixelSize) + posOffset
                pixelY = ((y + 1) * pixelSize) + posOffset

                # Draws the rectangle.
                with Image(width=pixelSize, height=pixelSize, background=pixelColour) as rect:
                    img.composite(image=rect, left=pixelX, top=pixelY)

    return img

def main():
    if len(sys.argv) != 5:
        sys.exit("Example usage: %s <canvas_size> <pixel_count> <pixel_colour> <out_file>" % sys.argv[0])

    canvasSize = int(sys.argv[1])
    pixelCount = int(sys.argv[2])
    pixelColour = sys.argv[3]
    outputFile = sys.argv[4]

    pixelSize = int(canvasSize / 6)

    with Color(pixelColour) as colour:
        with Color('#f0f0f0') as bgColour:
            with generate(canvasSize, pixelSize, pixelCount, colour, bgColour) as avatar:
                avatar.save(filename=outputFile)

if __name__ == "__main__":
    main()
