const express = require("express");
const multer = require("multer");
const cors = require("cors");
const { exec } = require("child_process");
const path = require("path");

const app = express();
app.use(cors());

const upload = multer({ dest: "uploads/" });

app.post("/predict", upload.single("image"), (req, res) => {

    const imgPath = req.file.path;
    const scriptPath = path.join(__dirname, "..", "model", "predict.py");

    const cmd = `py "${scriptPath}" "${imgPath}"`;

    console.log("Running:", cmd);

    exec(cmd, (error, stdout, stderr) => {

        console.log("STDOUT:", stdout);
        console.log("STDERR:", stderr);

        if (error) {
            console.log("EXEC ERROR:", error);
            return res.status(500).send(stderr || error.message);
        }

        try {
            const result = JSON.parse(stdout);
            res.json(result);
        } catch (e) {
            console.log("JSON Parse Error:", e);
            res.status(500).send(stdout);
        }
    });
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on port ${PORT}`);
});