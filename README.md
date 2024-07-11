# Image to ASCII Converter

This Python script converts an image to ASCII art and saves it as a text file. It uses the Python Imaging Library (PIL) to process the image and a custom exception to handle errors related to file extensions.

## Features

- Converts images to ASCII art
- Supports different scaling based on image size
- Customizable character mapping for ASCII art
- Error handling for missing file extensions

## Requirements

- Python 3.x
- Pillow library (`PIL`)

## Installation

1. Clone this repository or download the script.
2. Install the required library:

```sh
pip install Pillow
```

## Usage
Run the script from the command line with the following arguments:

```sh
python main.py <input_image> <output_text_file>
```

- <input_image>: Path to the input image file.
- <output_text_file>: Path to the output text file where the ASCII art will be saved.

### Example

```sh
python main.py girl-with-a-pearl-earring.jpg output.txt
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
