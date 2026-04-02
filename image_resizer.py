from PIL import Image
import os

# Configurações
image_path = "icon512x512.png"
output_path = "minha_imagem_redimensionada.png"
new_width = 700
new_height = 700  # deixe None para manter proporção

def resize_image(image_path, output_path, width, height=None):
    img = Image.open(image_path)
    
    if height is None:
        w_percent = (width / float(img.size[0]))
        height = int((float(img.size[1]) * float(w_percent)))
    
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    img.save(output_path)
    print(f"Imagem salva: {output_path}")

resize_image(image_path, output_path, new_width, new_height)
