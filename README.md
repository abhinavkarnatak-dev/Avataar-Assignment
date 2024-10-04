# Object Placement in Text-Conditioned Scenes

## Project Overview

This project uses Stable Diffusion Inpainting to place an object from an image with a white background into a text-conditioned scene. The generated image aligns with the provided text prompt, ensuring the object is placed naturally in the generated scene. The project also generates a video by zooming in/out on the object within the scene.

### Example Inputs and Outputs

- **Input Image**: 
  - A product image with a white background (e.g., a cooking appliance).
  
- **Text Prompt**: 
  - Example: "product in a kitchen used in meal preparation."
  
- **Output Image**: 
  - The object placed realistically in a kitchen setting.


## Approach

1. **Image Inpainting**:
   - The task is framed as an inpainting problem, where the provided object is placed naturally into a scene described by the text prompt.
   - I used the `StableDiffusionInpaintPipeline` from `diffusers` to modify the scene without altering the original object.

2. **Scene Generation**:
   - The object is blended into the scene generated from the text prompt. A mask is created to ensure the object remains unaltered, while the background is generated based on the prompt.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-link>
   cd <repository-name>
