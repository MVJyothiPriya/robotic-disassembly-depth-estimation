# Robotic Disassembly Depth Estimation

## Project Overview

This project explores **depth estimation for robotic disassembly tasks** using multiple state-of-the-art depth estimation models. The goal is to generate accurate depth maps from RGB images of objects that appear in robotic manipulation and disassembly environments.

Robotic disassembly of consumer electronics requires reliable **3D scene understanding**. However, real-world conditions such as:

- cluttered scenes
- reflective surfaces
- occlusions
- lighting variation

make depth estimation difficult.

This project evaluates several **pretrained depth estimation models** and compares their performance on robotic disassembly data.

---

# Repository Structure

```
robotic-disassembly-depth-estimation
│
├── DepthCrafter/
│   └── Source code and configuration files for the DepthCrafter model.
│
├── depth-capstone/
│   ├── scripts/
│   │   └── Python scripts used to run depth estimation models.
│   │
│   └── logs/
│       └── Small log files generated during experiments.
│
├── Depth_estimation.ipynb
│   └── Jupyter notebook containing experiments using MiDaS, DepthAnything, and DepthCrafter.
│
└── README.md
    └── Documentation describing the project and repository structure.
```

---

# Folder and File Descriptions

## DepthCrafter
Contains the implementation of the **DepthCrafter depth estimation model** used in the experiments.

## depth-capstone
Main project folder containing scripts and logs for running experiments.

### scripts
Python scripts used to:

- load pretrained depth estimation models
- process input frames
- generate depth maps
- save prediction outputs

### logs
Contains experiment log files generated during model runs.

---

# Notebook: Depth_estimation.ipynb

This notebook contains the **main experimental pipeline** of the project.

The notebook performs the following tasks:

1. Load pretrained depth estimation models
2. Run inference on robotic disassembly frames
3. Generate depth predictions
4. Compute evaluation metrics
5. Compare model performance visually and quantitatively

Models evaluated:

- **MiDaS**
- **DepthAnything**
- **DepthCrafter**

---

# Experiments and Results

## Baseline Model Comparison

Three pretrained depth estimation models were evaluated on the dataset.

| Model | Frames | Temporal Mean Abs Diff | Grad Mean | Lap Mean | HF Energy Ratio |
|------|------|------|------|------|------|
| DepthAnything | 891 | 0.015993 | 0.023660 | 0.014964 | 0.000022 |
| DepthCrafter | 891 | 0.019116 | 0.038047 | 0.023124 | 0.000075 |
| MiDaS | 891 | 0.055691 | 0.014597 | 0.007687 | 0.000029 |

### Observations

- **DepthAnything** produces more stable temporal predictions.
- **DepthCrafter** performs well on video sequences but shows slightly higher noise.
- **MiDaS** produces less stable results for this dataset.

---

## Fine-tuning Experiment

DepthAnything was further improved using **self-supervised fine-tuning** with:

- Temporal consistency loss
- Edge-aware smoothness regularization

### Baseline vs Fine-tuned Comparison

| Model | Frames | Temporal Mean Abs Diff | Grad Mean | Lap Mean | HF Energy Ratio |
|------|------|------|------|------|------|
| DepthAnything Baseline | 891 | 0.015993 | 0.023660 | 0.014964 | 0.000022 |
| DepthAnything Finetuned | 891 | 0.015335 | 0.035324 | 0.016339 | 0.000122 |

### Observations

- Fine-tuning slightly improved **temporal stability**
- However, the **high-frequency energy increased**, indicating additional noise

These results suggest that further optimization of the loss functions is needed.

---

# Depth Estimation Workflow

```
RGB Frame
     ↓
Pretrained Depth Model
(MiDaS / DepthAnything / DepthCrafter)
     ↓
Predicted Depth Map
     ↓
Metric Evaluation
```

Metrics used:

- Temporal stability
- Gradient statistics
- Laplacian statistics
- High-frequency energy ratio

---

# Large Files and Storage Note

Some directories were **not uploaded to GitHub** because they contain very large files (several gigabytes).

Excluded folders:

```
depth-capstone/data/
depth-capstone/experiments/
depth-capstone/**/checkpoints/
```

These folders contain:

- datasets
- trained model checkpoints
- experiment outputs

They are stored on **HyperGator storage** instead.

HyperGator path:

```
/blue/egn6933/mulakav/
```

---

# How to Navigate the Repository

1. Start with the notebook:

```
Depth_estimation.ipynb
```

2. The **DepthCrafter folder** contains model implementation.

3. The **depth-capstone/scripts** folder contains experiment scripts.

4. Logs can be found in:

```
depth-capstone/logs
```

---

# Future Work

Future improvements for this project include:

- Further fine-tuning of the depth estimation models
- Reducing **high-frequency noise in depth maps**
- Improving **temporal stability across frames**
- Optimizing the balance between temporal consistency loss and smoothness loss
- Integrating depth estimation with robotic disassembly pipelines

---

# Author

Venkata Jyothi Priya Mulaka  
M.S. Applied Data Science  
University of Florida
