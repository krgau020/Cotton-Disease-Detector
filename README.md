# 🌿 Cotton Disease Detector

Predict whether a cotton plant leaf is **healthy** or **diseased** using deep learning and transfer learning.

---

## 🚀 Project Overview

This project detects whether a cotton plant leaf is healthy or diseased using **two state-of-the-art CNN architectures**:

- ✅ **InceptionV3** — achieves **96% validation accuracy**
- ✅ **ResNet50** — slightly lower accuracy despite having more parameters

---

## 📂 Dataset

- Images of **healthy** and **diseased** cotton leaves.
- Preprocessed and split into **training**, **validation**, and **test** sets.

---

## ⚙️ Models Used

| Model         | Parameters  | Validation Accuracy |
|---------------|-------------|---------------------|
| InceptionV3   | ~21 million | ✅ **96%**           |
| ResNet50      | ~23 million | ~94%                |

**Conclusion:** InceptionV3 performs better with fewer parameters.

---

## 🧑‍💻 How to Run

1️⃣ **Clone the repo**

```bash
git clone https://github.com/krgau020/cotton-disease-detector.git
cd cotton-disease-detector

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Train the model

use files in notebook for training of model on custom data or you can use pretained model saved in models folder

4️⃣ Predict new images

refer notebook for predicting on image  OR use app.py 



**📈Results**
Validation Accuracy: ~96% (InceptionV3)

Test Accuracy: ~95%
