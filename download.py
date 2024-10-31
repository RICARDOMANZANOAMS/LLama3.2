from huggingface_hub import snapshot_download

snapshot_download(repo_id="meta-llama/Llama-3.2-11B-Vision-Instruct",
                  use_auth_token="your token",
                  local_dir="C:\\pathToSaveTheModel\\model\\")