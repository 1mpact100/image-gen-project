import os

from PIL import Image
from huggingface_hub import InferenceClient


HF_TOKEN = os.environ["HF_TOKEN"]

client = InferenceClient(token=HF_TOKEN)

image = client.text_to_image(
    prompt="A futuristic city at sunrise with glass towers, flying cars, and soft cinematic lighting",
    model="black-forest-labs/FLUX.1-schnell",
)

if isinstance(image, Image.Image):
    image.save("generated_image.png")
else:
    Image.open(image).save("generated_image.png")

print("Изображение успешно сохранено как 'generated_image.png'.")
