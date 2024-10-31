
In the following document, we review how to run locally llama3.2 with vision capabilities.

conda create --name llama3.2 python=3.10.12
conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia
pip install huggingface_hub
pip install sympy==1.13.1
pip install --upgrade transformers
pip install requests
pip install pillow
pip install psutil
pip install accelerate>=0.26.0

To dowload the llama 3.2 with vision go to the link in hugging face
https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct

Fill the form and wait to download
Generate the token to have access to the model

When Meta approves your request, go to download.py and paste the key to download