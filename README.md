# 🎯 Valorant YOLO Enemy Detection

An educational computer vision project that demonstrates **real-time enemy detection in Valorant** using **YOLOv5**.  
This project focuses on applying deep learning object detection techniques to game screen captures for learning and research purposes.

---

## 🚀 Project Overview

This repository contains a YOLOv5-based pipeline that detects enemy agents in the game **Valorant** from screen frames.  
The goal of this project is to explore:

- Object detection using deep learning
- Real-time inference with YOLOv5
- Computer vision applied to FPS game environments
- Dataset preparation and model experimentation

⚠️ **This project is strictly for educational and research purposes only.**

---

## 🧠 Model & Training

- **Model:** YOLOv5
- **Framework:** PyTorch
- **Approach:** Screen capture → Object detection → Bounding box visualization
- **Training:** Custom-labeled dataset created from gameplay frames

The model was trained to identify **enemy agents** appearing on the screen.

---

## 📂 Project Structure

Nice, let’s finish this properly 😄
Below is a clean, cool, recruiter-friendly README.md you can copy-paste directly.
It clearly explains YOLOv5, Valorant, and that trained images are inside yolov5/runs/.

I’m giving it in pure Markdown, ready to drop into README.md.

# 🎯 Valorant YOLO Enemy Detection

An educational computer vision project that demonstrates **real-time enemy detection in Valorant** using **YOLOv5**.  
This project focuses on applying deep learning object detection techniques to game screen captures for learning and research purposes.

---

## 🚀 Project Overview

This repository contains a YOLOv5-based pipeline that detects enemy agents in the game **Valorant** from screen frames.  
The goal of this project is to explore:

- Object detection using deep learning
- Real-time inference with YOLOv5
- Computer vision applied to FPS game environments
- Dataset preparation and model experimentation

⚠️ **This project is strictly for educational and research purposes only.**

---

## 🧠 Model & Training

- **Model:** YOLOv5
- **Framework:** PyTorch
- **Approach:** Screen capture → Object detection → Bounding box visualization
- **Training:** Custom-labeled dataset created from gameplay frames

The model was trained to identify **enemy agents** appearing on the screen.

---

## 📂 Project Structure



.
├── yolov5/
│ ├── models/ # YOLOv5 model definitions
│ ├── utils/ # Utility functions
│ ├── data/ # Dataset configs (YAML, scripts)
│ ├── runs/ # 🔥 Training & inference outputs
│ │ └── detect/
│ │ └── exp*/ # Trained images & detection results
│ └── ...
├── aimbot.py # Detection / inference script
├── convert_coco_to_yolo.py
├── download_data.py
└── README.md

---

## 🖼️ Trained Images & Results

All **training outputs, detection results, and predicted images** are stored inside:




Specifically:
- Detection images: `yolov5/runs/detect/`
- Each `exp` folder represents a separate experiment or run
- Images include bounding boxes drawn around detected enemies

These outputs are generated automatically by YOLOv5 during training and inference.

---

## ▶️ How It Works (High Level)

1. Capture game screen frames
2. Preprocess frames for YOLOv5
3. Run inference using the trained model
4. Display bounding boxes around detected enemies
5. Save output images in `yolov5/runs/`

---

## ⚙️ Setup & Usage (Basic)

```bash
pip install -r requirements.txt
python aimbot.py

Note: Dataset files and trained weights are not required to understand the code structure.

⚠️ Ethical & Legal Disclaimer

This project does NOT access game memory

No DLL injection, no reverse engineering, no game modification

Detection is performed only on screen-captured frames

Intended solely for learning, experimentation, and computer vision research

Not intended for competitive or unfair gameplay

📚 Learning Outcomes

Understanding YOLO-based object detection

Working with real-time computer vision pipelines

Managing ML project structure and outputs

Practical experience with PyTorch and YOLOv5

📌 Note

This repository is meant to showcase computer vision skills, not to promote cheating or misuse in online games.





