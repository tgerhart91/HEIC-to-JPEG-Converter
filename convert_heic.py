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
