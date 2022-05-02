import json

import torch
# from torch import nn
from torchvision import transforms
from flask import current_app
from pathlib import Path
from PIL import Image


transform = transforms.Compose([
    transforms.Resize((150, 150)),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5],
                         [0.5, 0.5, 0.5]) # normalize for pixel values to be between 0 and 1
])

with open('classes.json') as f:
	classes = json.load(f)

def get_model():
	model = torch.jit.load('model_jit.pt')

	model.eval()

	return model

def predict(fname, model):
	img_path = Path(current_app.config['UPLOAD_FOLDER'])/fname
	if img_path.is_file():		
		img = Image.open(img_path).convert('RGB')
		img = transform(img).unsqueeze(0)
		with torch.no_grad():
			class_idx = model(img).argmax(1)[0]

		return classes[class_idx]	
	return -1
