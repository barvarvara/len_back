import random
import string
from datetime import datetime
import torch
from diffusers import StableDiffusionPipeline, DDIMScheduler

# "stabilityai/stable-diffusion-2-base"
# WEIGHTS_DIR = "https://drive.google.com/drive/u/0/folders/1-H_dA30QdD8f0LvpxjLgzqae2ZnVU0Ys"
WEIGHTS_DIR = "https://huggingface.co/barvarvara/mezen-painting-ornament/tree/main"


def generate512x512(seed, prompt, num_samples=4,
                    negative_prompt="blurry, bad, deformed, bad, anatomy, ugly, bad spelling"):
    model_path = WEIGHTS_DIR

    pipe = StableDiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float16, revision="fp16")
    pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
    pipe.enable_xformers_memory_efficient_attention()
    # pipe = pipe.to("cuda")

    generator_with_seed = torch.Generator()
    generator_with_seed.manual_seed(seed)

    generated_images = (pipe(prompt, negative_prompt,
                             num_images_per_prompt=num_samples,
                             num_inference_steps=50,
                             height=512,
                             width=512,
                             generator=generator_with_seed,
                             guidance_scale=7.5)
                        .images)

    images = []
    for image in generated_images:
        dt = datetime.now()
        ts = datetime.timestamp(dt)
        randomString = ''.join(random.choices(string.ascii_lowercase, k=8))

        image_name = randomString + str(int(ts)) + '.png'
        images.append(image)

        image.save("../textures_app/media/" + image_name)

    return images
