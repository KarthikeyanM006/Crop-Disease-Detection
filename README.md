# 🌿 Crop Disease Detection Using Deep Learning

An AI-powered crop disease detection project that uses deep learning and computer vision to identify potential diseases in crop leaf images. The goal is to explore how image classification can support early disease identification and help farmers make more informed crop-management decisions.

## 📌 Project Overview

Crop diseases can affect agricultural productivity and crop quality. Identifying disease symptoms early can help farmers investigate problems and take appropriate action.

This project applies a deep-learning image classification approach to recognize crop diseases from leaf images. It uses **Python, PyTorch, and a ResNet-based convolutional neural network** to learn visual patterns from crop images and predict the corresponding class.

The project focuses on five major crops:

- 🌾 Wheat
- 🌾 Rice
- 🌿 Cotton
- 🎋 Sugarcane
- 🌽 Maize

## ✨ Key Features

- **Image-based disease classification:** Uses crop leaf images as model input.
- **Multi-crop focus:** Covers wheat, rice, cotton, sugarcane, and maize.
- **Deep-learning approach:** Applies convolutional neural networks to image classification.
- **PyTorch implementation:** Supports model training, validation, and inference.
- **Image preprocessing:** Prepares images in a consistent format for model input.
- **GPU-assisted training:** Can use a compatible NVIDIA GPU to accelerate model training.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PyTorch | Deep-learning model development |
| ResNet50 | Image classification architecture |
| Torchvision | Pretrained models and image transformations |
| NumPy | Numerical operations |
| Matplotlib | Visualization of training results |
| Jupyter Notebook | Model development and experimentation |
| CUDA | GPU acceleration, when supported |

## ⚙️ How It Works

The general workflow consists of the following steps:

1. **Dataset preparation:** Collect and organize labeled crop leaf images.
2. **Image preprocessing:** Resize and normalize images to match the model's input requirements.
3. **Model development:** Configure a ResNet-based image classification model.
4. **Model training:** Train the model on the prepared dataset.
5. **Model evaluation:** Evaluate its predictions on validation or test images.
6. **Disease prediction:** Pass a crop leaf image to the trained model to obtain a predicted class.

## 📂 Project Structure

The repository may be organized as follows. Adjust the filenames and folders to match the actual files in this repository.

```text
Crop-Disease-Detection/
│
├── dataset/                 # Crop image dataset
├── notebooks/               # Training and experiments
├── models/                  # Saved model weights
├── outputs/                 # Evaluation results and plots
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible Python version
- pip
- Git
- Jupyter Notebook or JupyterLab
- An NVIDIA GPU with compatible PyTorch/CUDA support (optional)

### 1. Clone the repository

```bash
git clone https://github.com/KarthikeyanM006/Crop-Disease-Detection.git
cd Crop-Disease-Detection
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

If the repository contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the packages required by your notebook and model:

```bash
pip install torch torchvision numpy matplotlib pillow jupyter
```

### 4. Open the notebook

```bash
jupyter notebook
```

Open the project's training or inference notebook and follow its instructions.

**Note:** The dataset location, model-weight filename, and notebook names depend on the files included in the repository.

## 🧪 Model Training and Prediction

The model-training workflow generally includes:

- Loading labeled crop images.
- Applying preprocessing and data augmentation, where appropriate.
- Initializing the ResNet-based model.
- Training with an appropriate optimizer and loss function.
- Monitoring training and validation performance.
- Saving the trained model weights.
- Loading the saved weights for prediction on new images.

Use the exact class labels and preprocessing transformations from the training pipeline when running inference.

## 📊 Results and Evaluation

Model performance should be evaluated using a separate validation or test dataset.

Useful evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Actual results should be reported only after evaluation. Performance may vary with image quality, dataset distribution, crop variety, and real-world lighting conditions.

## 🌱 Applications

Potential applications of crop disease classification include:

- Supporting preliminary crop health assessment.
- Helping students explore agricultural AI.
- Demonstrating computer vision for precision agriculture.
- Providing a foundation for future farmer-oriented crop monitoring tools.

## 🔮 Future Enhancements

- Develop a simple web interface for uploading crop images.
- Add disease-specific information and verified treatment guidance.
- Evaluate performance on real-world field images.
- Improve robustness to different backgrounds and lighting conditions.
- Explore mobile deployment for easier field use.
- Provide multilingual information for farmers.

## ⚠️ Limitations

This project is an experimental deep-learning application. A model prediction is not a definitive agricultural diagnosis. Predictions may be unreliable for unfamiliar crop varieties, poor-quality images, or diseases not represented in the training data.

Farmers should verify suspected diseases with a qualified agricultural expert before making treatment decisions.

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork this repository.
2. Create a new branch for your changes.
3. Commit your changes.
4. Push the branch to your fork.
5. Open a pull request describing your improvements.

## 👨‍💻 Author

**Karthikeyan M**

Computer Science and Engineering  
Kongu Engineering College

- GitHub: [@KarthikeyanM006](https://github.com/KarthikeyanM006)
- Project Repository: [Crop Disease Detection](https://github.com/KarthikeyanM006/Crop-Disease-Detection)

---

⭐ If you find this project useful for learning about deep learning and agricultural applications, consider starring the repository.
