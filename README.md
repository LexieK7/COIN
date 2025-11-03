# 📌 COIN: A Controllable Cytology Image Generation Foundation Model

<p align="center"> <img src="https://img.shields.io/badge/Cytology-Foundation--Model-green" /> <img src="https://img.shields.io/badge/Generative-AI-FF69B4" /> <img src="https://img.shields.io/badge/Data-Augmentation-Effective-orange" /> 
  
### 🌟 Project Highlights

COIN is a foundation model for controllable cytology image generation, trained on over 112,000 cytology image-report pairs across 16 anatomical sites.
It enables privacy-preserving, realistic synthetic cytology image generation driven by diagnostic reports.

The pretrained COIN model weights are available on [Hugging Face](https://huggingface.co/LexieK/COIN).  
You can request access and download the weights directly from the link above.

### 📝 Abstract



### 🛠️ Getting started

Clone this repo:

```
https://github.com/LexieK7/COIN.git
cd COIN
```



### 📂 Usage
### 1️⃣ Generate Cytology Images from texts

```
from diffusers import DiffusionPipeline
import torch
import os

sdxl_base_model = "./sd_xl_1-0"   
lora_model_path = "MODEL PATH"  
save_folder = "./generated_images"
prompt = "No intraepithelial lesion or malignancy (NILM)."
guidance_scale = 7.5
num_inference_steps = 50

pipe = DiffusionPipeline.from_pretrained(sdxl_base_model)
pipe.to("cuda")
pipe.load_lora_weights(lora_model_path)

save_path = os.path.join(save_folder, "example.jpg")
image = pipe(prompt, num_inference_steps=num_inference_steps, guidance_scale=guidance_scale).images[0]
image.save(save_path)

```



### 📄 Citation

If you find this work useful, please cite us:
