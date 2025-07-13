from PIL import Image
import exifread

# Select image file
image_path = input("Enter the path to your image file: ")

# Show basic image info
with Image.open(image_path) as img:
    print(f"\n Image Format: {img.format}")
    print(f" Size: {img.size[0]}x{img.size[1]}")
    print(f" Mode: {img.mode}")

# Show EXIF metadata
print("\n EXIF Metadata:")
with open(image_path, 'rb') as f:
    tags = exifread.process_file(f)
    for tag in tags:
        if tag not in ("JPEGThumbnail", "TIFFThumbnail", "Filename", "EXIF MakerNote"):
            print(f"{tag}: {tags[tag]}")
