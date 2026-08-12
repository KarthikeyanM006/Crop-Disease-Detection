import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImage = (e) => {
    const file = e.target.files[0];

    if (!file) return;

    setImage(file);
    setPreview(URL.createObjectURL(file));
    setResult(null);
  };

  const predictImage = async () => {
    if (!image) {
      alert("Please choose an image");
      return;
    }

    const formData = new FormData();
    formData.append("image", image);

    setLoading(true);
    setResult(null);

    try {
      const res = await axios.post(
        "https://crop-disease-detection-p2pe.onrender.com/predict",
        formData
      );

      setResult(res.data);
    } catch (error) {
      console.error("Prediction Error:", error);

      if (error.response) {
        alert(
          `Prediction failed: ${error.response.data?.error || error.response.statusText}`
        );
      } else {
        alert("Prediction failed. Please check the backend server.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="main">
      <div className="card">
        <h1>🌿 Crop Disease Detection</h1>

        <p>AI Based Smart Farming Solution</p>

        <input
          type="file"
          accept="image/*"
          onChange={handleImage}
        />

        {preview && (
          <img
            src={preview}
            alt="Crop preview"
            className="preview"
          />
        )}

        <button
          onClick={predictImage}
          disabled={loading}
        >
          {loading ? "Predicting..." : "Predict"}
        </button>

        {result && (
          <div className="result">
            <h2>{result.disease}</h2>
            <h3>{result.confidence}% Confidence</h3>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;