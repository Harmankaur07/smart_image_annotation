import os

def get_image_info(image, uploaded_file):
    width, height = image.size
    image_format = image.format
    image_mode = image.mode

    # File size in KB
    uploaded_file.seek(0, os.SEEK_END)
    file_size = uploaded_file.tell() / 1024
    uploaded_file.seek(0)

    return {
        "width": width,
        "height": height,
        "format": image_format,
        "mode": image_mode,
        "size": file_size
    }
    
    
    
    