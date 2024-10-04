# Object Placement in Text-Conditioned Scenes

## Project Overview

This project uses **Stable Diffusion Inpainting** to place an object from an image with a white background into a text-conditioned scene. The goal is to generate realistic product images for e-commerce purposes, ensuring the object is integrated naturally into the scene.

---

## Installation

### 1. Clone the Repository
```bash
git clone <repository-link>
cd <repository-folder>
```

### 2. Install Dependencies

Make sure you have `pip` installed, then install the dependencies by running:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not provided, manually install the required packages:

```bash
pip install torch diffusers accelerate transformers pillow
```

---

## Execution

To generate an image, use the following command:

```bash
python run.py --image ./input_image.jpg --text-prompt "product in a kitchen used in meal preparation" --output ./generated.png
```

### Command-Line Arguments
- `--image`: Path to the input image (with the object on a white background).
- `--text-prompt`: The scene description to condition the generated background.
- `--output`: Path to save the final generated image.

---

## Example Command

```bash
python run.py --image ./example.jpg --text-prompt "product in a kitchen used in meal preparation" --output ./generated.png
```

---

## Approach to Solving the Problem

### 1. Initial Setup
- The task required using a generative model to place a product image into a scene specified by a text prompt.
- I chose **Stable Diffusion Inpainting** to mask the object and generate the scene around it.

### 2. Realism Challenges
- **Aspect Ratio & Placement**: Ensuring the object was scaled properly and placed naturally in the generated scene.
- **Lighting Consistency**: Aligning the lighting and shadows of the object with the scene.

---

## Results

### Generated Image

- (Attach the generated image here)
- The object was successfully placed in the scene, aligning with the prompt and maintaining realism.

---

## Challenges & Improvements

### Challenges
- **Aspect Ratio**: Incorrect placement and scaling of the object in the scene during initial tests.
- **Lighting Mismatch**: Some generated scenes had inconsistent lighting between the object and the scene.

### Improvements
- Used a more precise **text-prompt** to improve the generated scene.
- Fine-tuned the **masking process** to preserve the object’s details better.



## Conclusion

This project demonstrates how generative AI can automate product photography for e-commerce. While it produces promising results, further refinements are needed in ensuring aspect ratio and lighting consistency to achieve a higher level of realism.
```
