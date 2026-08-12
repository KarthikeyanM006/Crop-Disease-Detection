const express = require("express");
const multer = require("multer");
const cors = require("cors");
const { exec } = require("child_process");
const path = require("path");

const app = express();

app.use(cors());
app.use(express.json());

const upload = multer({ dest: "uploads/" });

// Health check
app.get("/", (req, res) => {
    res.json({
        status: "success",
        message: "Crop Disease Detection API is running"
    });
});

// Prediction endpoint
app.post("/predict", upload.single("image"), (req, res) => {

    if (!req.file) {
        return res.status(400).json({
            error: "No image uploaded"
        });
    }

    const imgPath = req.file.path;
    const scriptPath = path.join(__dirname, "..", "model", "predict.py");

    // Linux uses python3 instead of Windows "py"
    const cmd = `python3 "${scriptPath}" "${imgPath}"`;

    console.log("Running:", cmd);

    exec(cmd, (error, stdout, stderr) => {

        console.log("STDOUT:", stdout);
        console.log("STDERR:", stderr);

        if (error) {
            console.log("EXEC ERROR:", error);

            return res.status(500).json({
                error: stderr || error.message
            });
        }

        try {
            const result = JSON.parse(stdout);
            res.json(result);
        } catch (e) {
            console.log("JSON Parse Error:", e);

            res.status(500).json({
                error: "Invalid prediction response",
                output: stdout
            });
        }
    });
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on port ${PORT}`);
});