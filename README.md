# Improving Depth Estimation for Robotic Disassembly

## 📌 Project Overview

This project focuses on improving monocular depth estimation for robotic disassembly tasks using real-world, unlabeled consumer electronics video data. Accurate depth estimation is essential for robotic manipulation, including object grasping and safe disassembly. However, real-world conditions such as clutter, reflections, occlusions, and lighting variations make depth estimation challenging. This project evaluates multiple state-of-the-art models and proposes a practical solution to improve depth quality.


## 🎯 Project Goals

* Evaluate state-of-the-art depth estimation models
* Analyze performance on real-world disassembly data
* Identify failure modes such as noise and instability
* Improve depth predictions using a robust approach
* Build a complete pipeline and demo system


## 🧠 Models Used

* **MiDaS (Monocular Depth Estimation via Transformers)**
  Robust general-purpose model but showed temporal instability

* **Depth Anything**
  Large-scale foundation model with strong generalization
  Selected as the final model

* **DepthCrafter (Baseline)**
  Video-based depth estimation model but produced higher noise


## 📊 Dataset

* Source: Consumer electronics disassembly videos
* Type: Unlabeled real-world data
* Size: ~10,000+ frames

### Preprocessing Steps

* Frame extraction from videos
* Blur detection and removal
* Image resizing


## 🔄 Project Pipeline

Video Input → Frame Extraction → Blur Filtering → Depth Estimation (MiDaS / Depth Anything / DepthCrafter) → Depth Maps → Smoothing → Evaluation → Improved Depth Output


## ⚙️ Implementation

### Main Notebook

* `Depth_estimation.ipynb` → Final complete pipeline


### Repository Structure

```text
robotic-disassembly-depth-estimation/
│
├── README.md
├── Depth_estimation.ipynb
├── HWCOE-Poster-Template-Vertical-24x36-1.pdf
│
├── DepthCrafter/
│   ├── benchmark/
│   ├── dc_videos/                ← Final depth outputs and video results are stored here
│   ├── depthcrafter/
│   ├── examples/
│   ├── tools/
│   ├── unit_tests/
│   ├── visualization/
│   ├── .gitattributes
│   ├── .gitignore
│   ├── .python-version
│   ├── LICENSE
│   ├── README.md
│   ├── app.py
│   ├── pyproject.toml
│   ├── run.py
│   └── uv.lock
│
└── depth-capstone/
    ├── app/
    ├── checkpoints/
    ├── data/
    ├── experiments/
    └── scripts/
```

**Note:**

* The folder `DepthCrafter/dc_videos/` contains the **generated depth estimation video outputs and final visual results**.
* Due to large file sizes, these outputs may not be fully available on GitHub and are stored in HyperGator.



## 🧪 Attempted Approaches

* Fine-tuning Depth Anything
* Self-supervised learning
* Teacher-based training

These approaches did not provide consistent improvements and sometimes increased noise, so they were not selected.


## Final Solution: Strong Smoothing

A post-processing approach was applied to improve depth outputs:

* Gaussian spatial smoothing (reduces noise)
* Temporal smoothing (reduces flicker)
* 16-bit depth precision (preserves details)

### Outcome

* Cleaner depth maps
* Reduced noise
* Improved temporal consistency


## 📈 Evaluation Metrics

* Temporal Stability (lower is better)
* High-Frequency Energy Ratio (noise measurement)


## 📊 Final Results

| Metric             | Baseline | Improved |
| ------------------ | -------- | -------- |
| Temporal Stability | 0.01991  | 0.01441  |
| HF Energy Ratio    | 3.6e-5   | 2.1e-5   |

### Improvements

* 27.6% improvement in temporal stability
* 41.7% reduction in noise


## 📁 Results Storage

All final outputs and evaluation results are stored in:

```
depth-capstone/experiments/
```

Includes:

* Depth maps
* Evaluation metrics
* Baseline vs improved comparisons

Note: Large files are stored externally (HyperGator).


## 🎥 Final Demo Video

https://uflorida-my.sharepoint.com/personal/mulakav_ufl_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fmulakav%5Fufl%5Fedu%2FDocuments%2FRecordings%2Ffinal%20presentation%2D20260413%5F225712%2DMeeting%20Recording%2FExports%2Ffinal%20presentation%2D20260413%5F225712%2DMeeting%20Recording%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E4a676b6b%2Dca09%2D4166%2D98f6%2D65fb2a945b43

---

## 🌐 Blog

Project explanation and visual results:

https://mvjyothipriya.github.io/Improving-Depth-Estimation-for-Robotic-Disassembly_Blog/


## 💻 Demo Application

Located in:

```
depth-capstone/app/
```

Features:

* Input image
* Depth prediction
* Improved output visualization


## ⚠️ Large Files Note

The following directories are not included in GitHub due to size:

```
depth-capstone/data/
depth-capstone/experiments/
depth-capstone/checkpoints/
```

Stored at:

```
/blue/egn6933/mulakav/
```


## 🌍 Applications

* Robotic disassembly
* Industrial automation
* Depth-based manipulation
* Scene understanding

## 🔍 Key Learnings

* Real-world data is significantly more complex than benchmark datasets
* Pretrained models do not generalize perfectly
* Simpler solutions can outperform complex training approaches
* Visual quality is as important as numerical metrics


## 🔮 Future Work

* Real-time depth estimation
* Integration with robotic systems
* Advanced temporal modeling
* Further noise reduction


## 👩‍💻 Author

Venkata Jyothi Priya Mulaka
M.S. Applied Data Science
University of Florida

Email: [mulakav@ufl.edu](mailto:mulakav@ufl.edu)
Email: [mvjpriya@gmail.com](mailto:mvjpriya@gmail.com)
