import torch
from transformers import MllamaForConditionalGeneration, AutoProcessor
from PIL import Image
import time
start_time = time.time()
model_id="C:\\PathToModelDirectory\\model\\"
imageName="C:\\PathToImages\\images\\cats.jpg"

model=MllamaForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

processor=AutoProcessor.from_pretrained(model_id)


image=Image.open(imageName)

messageDataStructure=[
    {"role":"user","content":[
        {"type":"image"},
        {"type":"text", "text":"How many cats are in the image"}


    ]}
]

textInput=processor.apply_chat_template(messageDataStructure,add_generation_prompt=True)

inputs=processor(image,textInput,return_tensors="pt").to(model.device)

output=model.generate(**inputs,max_new_tokens=2000)

generatedOuput=processor.decode(output[0])

print(generatedOuput)
# End the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

