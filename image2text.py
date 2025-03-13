from transformers import pipeline

captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
cap = captioner("https://huggingface.co/datasets/Narsil/image_dummy/resolve/main/parrots.png")
print(cap[0]['generated_text'])