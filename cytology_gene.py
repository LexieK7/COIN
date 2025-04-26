from diffusers import DiffusionPipeline
import torch
import pandas as pd
import shutil
import os


model_path = "MODEL PATH"
pipe = DiffusionPipeline.from_pretrained("./sd_xl_1-0/")  # PATH TO PRE-TRAINED SDXL 1.0
pipe.to("cuda") 
pipe.load_lora_weights(model_path)  


df = pd.read_excel("./text_content.xlsx")


save_folder = "SAVE PATH"
os.makedirs(save_folder, exist_ok=True)


for index, row in df.iterrows():
    base_img_name = row.iloc[0].split('/')[-1].split('.')[0]  
    prompt = str(row.iloc[1])  
 
    for i in range(1, 2):  #4/20
        save_path = os.path.join(save_folder, f"{base_img_name}_{i}.jpg")

      
        if os.path.exists(save_path):
            print(f"Skipping {save_path}, already exists.")
            continue

        print(f"Generating: {save_path} -> {prompt}")


        image = pipe(prompt, num_inference_steps=50, guidance_scale=7.5).images[0]
        image.save(save_path)  