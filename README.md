# GitHub Avatar Generator
A GitHub-esque avatar image generator written in Python.

![Example 1](/images/1.png)
![Example 2](/images/2.png)
![Example 3](/images/3.png)
![Example 4](/images/4.png)
![Example 5](/images/5.png)
![Example 6](/images/6.png)

## Installation

1. Install MagickWand:
    ```
    sudo apt-get install libmagickwand-dev
    ```
    Instructions for installing MagickWand [are also available for Mac, Windows, and others](http://docs.wand-py.org/en/0.4.1/guide/install.html).

2. Install the Python Wand package:
    ```
    pip install wand
    ```

3. Clone repository:
    ```
    git clone https://github.com/innix/github-avatar-generator.git
    ```


## Usage
An example script is provided to demonstrate usage. The example creates a single avatar image and saves it to a file.
```
python example.py <canvas_size> <block_count> <output_filename>
```

| Parameter       | Summary                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------ |
| canvas_size     | The size (width and height) of the image in pixels.                                        |
| block_count     | The number of colored blocks to use in the image.                                          |
| output_filename | The output image file path.                                                                |

Example:
```
python example.py 420 12 avatar_01.png
```

## License
You may use GitHub Avatar Generator under the terms of the MIT License (see [LICENSE](LICENSE)).
