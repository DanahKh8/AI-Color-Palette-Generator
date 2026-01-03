# AI Color Palette Generator

> **Extract aesthetic color schemes from any image using Machine Learning.**

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=flat&logo=opencv)
![Scikit-Learn](https://img.shields.io/badge/Sklearn-KMeans-orange?style=flat&logo=scikit-learn)

## Demo
**Input Image vs. AI Extracted Palette**
![Demo Preview](demo_preview.png)
*(The AI analyzes pixel data to find the 5 dominant colors mathematically)*

## How It Works
This tool doesn't just "guess" colors. It uses **K-Means Clustering** (an Unsupervised Machine Learning algorithm) to group thousands of pixels into clusters based on their RGB values.
1.  **Load Image:** Reads raw pixel data using OpenCV.
2.  **Cluster:** The AI finds "centroids" (centers of color density).
3.  **Extract:** Returns the Hex Codes of the most dominant clusters.

## Installation
```bash
git clone [https://github.com/DanahKh8/AI-Color-Palette-Generator.git](https://github.com/DanahKh8/AI-Color-Palette-Generator.git)
pip install -r requirements.txt
python main.py