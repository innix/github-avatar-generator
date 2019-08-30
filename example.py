#!/usr/bin/env python

'''
Generates GitHub-esque avatar images.

Usage:
    example.py <canvas_size> <block_count> <output_filename>

    canvas_size - The size (width and height) of the image in pixels.
    block_count - The number of colored blocks to use in the image.
    output_filename - The output image file path.

Example:
    example.py 420 12 test.png
'''

import avatargen
import sys

def main():
    if len(sys.argv) != 4:
        sys.exit("Example usage: " + sys.argv[0] + \
                 " <canvas_size> <block_count> <output_filename>")

    canvas_size = int(sys.argv[1])
    block_size = int(canvas_size / 6)

    block_count = int(sys.argv[2])
    output = sys.argv[3]

    with avatargen.generate(size=canvas_size,
                            block_size=block_size,
                            block_count=block_count) as avatar:
        avatar.save(output)

if __name__ == "__main__":
    main()
