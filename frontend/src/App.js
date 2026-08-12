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
    setImage(file);
    setPreview(URL.createObjectURL(file));
    setResult(null);
  };

  const predictImage = async () => {
    if (!image) return alert("Please choose image");

    const formData = new FormData();
    formData.append("image", image);

    setLoading(true);

    try {
      const res = await axios.post(
        "http://localhost:5000/predict",
        formData
      );

      setResult(res.data);
    } catch (error) {
      alert("Prediction failed");
    }

    setLoading(false);
  };

  return (
    <div className="main">

      <div className="card">

        <h1>🌿 Crop Disease Detection</h1>
        <p>AI Based Smart Farming Solution</p>

        <input type="file" onChange={handleImage} />

        {preview && (
          <img src={preview} alt="preview" className="preview" />
        )}

        <button onClick={predictImage}>
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