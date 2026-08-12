# ==========================================
# model/predict.py
# EfficientNet-B3 Version
# Full Fixed for React + Node.js
# ==========================================

import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import json
import sys
import os

# -----------------------------
# GET IMAGE PATH FROM NODE.JS
# -----------------------------
img_path = sys.argv[1]

# -----------------------------
# BASE FOLDER
# -----------------------------
base = os.path.dirname(__file__)

# -----------------------------
# MODEL + CLASSES PATH
# -----------------------------
model_path = os.path.join(
    base,
    "ultra_best_efficientnet_b3.pth"
)

class_path = os.path.join(
    base,
    "classes.json"
)

# -----------------------------
# DEVICE
# -----------------------------
device = torch.device("cpu")

# -----------------------------
# LOAD CLASSES
# -----------------------------
with open(class_path, "r") as f:
    classes = json.load(f)

num_classes = len(classes)

# -----------------------------
# LOAD EfficientNet-B3
# -----------------------------
model = models.efficientnet_b3(
    weights=None
)

# -----------------------------
# REPLACE CLASSIFIER
# SAME AS TRAINING
# -----------------------------
model.classifier = nn.Sequential(

    nn.Dropout(0.5),

    nn.Linear(
        model.classifier[1].in_features,
        1024
    ),

    nn.ReLU(),

    nn.BatchNorm1d(1024),

    nn.Dropout(0.4),

    nn.Linear(1024, num_classes)
)

# -----------------------------
# LOAD TRAINED WEIGHTS
# -----------------------------
model.load_state_dict(
    torch.load(
        model_path,
        map_location=device
    )
)

model = model.to(device)

model.eval()

# -----------------------------
# IMAGE PREPROCESS
# SAME AS TRAINING
# -----------------------------
transform = transforms.Compose([

    transforms.Resize((300,300)),

    transforms.ToTensor(),

    transforms.Normalize(
        [0.485,0.456,0.406],
        [0.229,0.224,0.225]
    )
])

# -----------------------------
# LOAD IMAGE
# -----------------------------
img = Image.open(img_path).convert("RGB")

img = transform(img).unsqueeze(0)

img = img.to(device)

# -----------------------------
# PREDICTION
# -----------------------------
with torch.no_grad():

    outputs = model(img)

    probs = torch.softmax(outputs, dim=1)

    confidence, pred = torch.max(probs, 1)

# -----------------------------
# RESULT
# -----------------------------
result = {
    "disease": classes[pred.item()],
    "confidence": round(
        confidence.item() * 100,
        2
    )
}

# -----------------------------
# SEND RESULT TO NODE.JS
# -----------------------------
print(json.dumps(result))