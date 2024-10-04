import argparse
import torch
from PIL import Image
from diffusers import StableDiffusionInpaintPipeline

def load_image(image_path):
    return Image.open(image_path).convert("RGB")

def inpaint_scene(pipeline, image, text_prompt, output_path):
    mask = Image.new("L", image.size, 255)
    result = pipeline(prompt=text_prompt, image=image, mask_image=mask).images[0]
    result.save(output_path)

def main():
    parser = argparse.ArgumentParser(description="Generate image using Stable Diffusion")
    parser.add_argument('--image', type=str, required=True, help='Path to the input image')
    parser.add_argument('--text-prompt', type=str, required=True, help='Text prompt for scene generation')
    parser.add_argument('--output', type=str, required=True, help='Path to save the generated image')

    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionInpaintPipeline.from_pretrained("stabilityai/stable-diffusion-2-inpainting").to(device)
    image = load_image(args.image)
    inpaint_scene(pipe, image, args.text_prompt, args.output)

if __name__ == "__main__":
    main()