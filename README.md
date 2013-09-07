# GitHub Avatar Generator
A GitHub-esque avatar image generator written in Python.


## Installation
1. Install MagickWand and Wand:
```
apt-get install libmagickwand-dev
pip install wand
```

2. Install NumPy:
```
pip install numpy
```

3. Clone repository:
```
git clone https://github.com/innix/GitHub-Avatar-Generator.git
```


## Usage
The current script has a straightforward usage for creating a single avatar image and saving it to a file.
```
python avatar-gen.py <canvas_size> <pixel_count> <pixel_colour> <out_file>
```

| Parameter    | Summary                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------ |
| canvas_size  | The width and height of the avatar image in pixels.                                        |
| pixel_count  | The number of (enlarged) pixels to use in the image.                                       |
| pixel_colour | The colour of the pixels. This may be a named colour (red, orange, etc.) or hex (#ff0000). |
| out_file     | The output image.                                                                          |

Example:
```
python avatar-gen.py 420 12 "#a30000" avatar_01.png
```

## License
You may use GitHub Avatar Generator under the terms of the MIT License (see [LICENSE](LICENSE)).
