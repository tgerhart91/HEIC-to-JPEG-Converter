# HEIC to JPEG Converter  

A simple Python script to convert HEIC images to JPEG using ImageMagick and Wand.

## Installation

1. Install ImageMagick

Download and isntall [ImageMagick](https://imagemagick.org/script/download.php)
During installation, make sure to check:

✅ Install legacy utilities  
✅ Add ImageMagick to system PATH  

2. Install Python Dependencies

Run the following command to install the required Python package:

```sh
pip install Wand
```

## Usage

Run the script from the command line:

```sh
python convert_heic.py input.heic
```

This will convert input.heic to input.jpg in the same directory.

To specify an output filename:

```sh
python convert_heic.py input.heic output.jpg
```

## Script Details

```sh
from wand.image import Image
import sys
import os

def convert_heic_to_jpg(input_file, output_file=None):
    if not output_file:
        output_file = os.path.splitext(input_file)[0] + ".jpg"
    
    try:
        with Image(filename=input_file) as img:
            img.format = 'jpeg'
            img.save(filename=output_file)
        print(f"Converted {input_file} → {output_file}")
    except Exception as e:
        print(f"Error converting {input_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_heic.py input.heic [output.jpg]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_heic_to_jpg(input_file, output_file)
```

## Troubleshooting

If you get an error about ImageMagick missing, make sure it is added to your system PATH.

If you get an error about wand, ensure ImageMagick is correctly installed and try reinstalling wand:

```sh
pip uninstall Wand
pip install Wand
```

## License

This project is open-source and available under the MIT License.

