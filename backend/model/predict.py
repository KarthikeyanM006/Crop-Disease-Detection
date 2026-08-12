import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import json
import sys
import os

# ==========================================
# GET IMAGE PATH FROM NODE.JS
# ==========================================

if len(sys.argv) < 2:
    print(json.dumps({
        "error": "Image path not provided"
    }))
    sys.exit(1)

img_path = sys.argv[1]

# ==========================================
# BASE FOLDER
# ==========================================

base = os.path.dirname(os.path.abspath(__file__))

# ==========================================
# MODEL + CLASSES PATH
# ==========================================

model_path = os.path.join(
    base,
    "ultra_best_efficientnet_b3.pth"
)

class_path = os.path.join(
    base,
    "classes.json"
)

# ==========================================
# CHECK FILES
# ==========================================

if not os.path.exists(model_path):
    print(json.dumps({
        "error": f"Model file not found: {model_path}"
    }))
    sys.exit(1)

if not os.path.exists(class_path):
    print(json.dumps({
        "error": f"Classes file not found: {class_path}"
    }))
    sys.exit(1)

if not os.path.exists(img_path):
    print(json.dumps({
        "error": f"Image file not found: {img_path}"
    }))
    sys.exit(1)

# ==========================================
# CPU OPTIMIZATION FOR RENDER
# ==========================================

device = torch.device("cpu")

# Limit CPU threads to reduce memory usage
torch.set_num_threads(1)

# ==========================================
# LOAD CLASSES
# ==========================================

with open(class_path, "r") as f:
    classes = json.load(f)

num_classes = len(classes)

# ==========================================
# CREATE EfficientNet-B3
# ==========================================

model = models.efficientnet_b3(
    weights=None
)

# ==========================================
# REPLACE CLASSIFIER
# SAME AS TRAINING
# ==========================================

model.classifier = nn.Sequential(
    nn.Dropout(0.5),

    nn.Linear(
        model.classifier[1].in_features,
        1024
    ),

    nn.ReLU(),

    nn.BatchNorm1d(1024),

    nn.Dropout(0.4),

    nn.Linear(
        1024,
        num_classes
    )
)

# ==========================================
# LOAD TRAINED MODEL
# ==========================================

try:
    state_dict = torch.load(
        model_path,
        map_location=device
    )

    model.load_state_dict(state_dict)

except Exception as e:
    print(json.dumps({
        "error": f"Failed to load model: {str(e)}"
    }))
    sys.exit(1)

# ==========================================
# MOVE MODEL TO CPU
# ==========================================

model = model.to(device)

model.eval()

# ==========================================
# IMAGE PREPROCESSING
# SAME AS TRAINING
# ==========================================

transform = transforms.Compose([
    transforms.Resize((300, 300)),

    transforms.ToTensor(),

    transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
    )
])

# ==========================================
# LOAD IMAGE
# ==========================================

try:
    img = Image.open(img_path).convert("RGB")
    img = transform(img).unsqueeze(0)
    img = img.to(device)

except Exception as e:
    print(json.dumps({
        "error": f"Failed to process image: {str(e)}"
    }))
    sys.exit(1)

# ==========================================
# PREDICTION
# ==========================================

try:

    with torch.inference_mode():

        outputs = model(img)

        probs = torch.softmax(outputs, dim=1)

        confidence, pred = torch.max(
            probs,
            dim=1
        )

    # ==========================================
    # RESULT
    # ==========================================

    result = {
        "disease": classes[pred.item()],
        "confidence": round(
            confidence.item() * 100,
            2
        )
    }

    # ==========================================
    # SEND RESULT TO NODE.JS
    # ==========================================

    print(json.dumps(result))

except Exception as e:

    print(json.dumps({
        "error": f"Prediction failed: {str(e)}"
    }))

    sys.exit(1)