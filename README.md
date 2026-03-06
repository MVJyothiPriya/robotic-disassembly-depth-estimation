# Robotic Disassembly Depth Estimation

## Project Overview

This project explores **depth estimation for robotic disassembly tasks** using multiple state-of-the-art depth estimation models. The goal is to generate accurate depth maps from RGB images of objects that may appear in robotic manipulation and disassembly environments.

Robotic disassembly of consumer electronics requires reliable **3D understanding of scenes**. However, many real-world conditions such as occlusion, clutter, reflections, and lighting variation make depth estimation difficult.

To address this challenge, this project evaluates several **pretrained depth estimation models** and compares their performance on real-world robotic disassembly data.

The experiments and analysis are implemented in a Jupyter notebook.

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

## DepthCrafter/

This folder contains the implementation and supporting files for the **DepthCrafter depth estimation model**.

DepthCrafter is one of the models evaluated in this project for generating depth maps from RGB images.

---

## depth-capstone/

This is the main project directory containing scripts and logs related to the experiments.

### scripts/

This folder contains Python scripts used to:

- load pretrained depth estimation models
- process input images
- run inference
- generate depth maps
- save results for further analysis

### logs/

This folder contains small log files generated during model execution.

---

## Depth_estimation.ipynb

This Jupyter notebook contains the **main experimental workflow** of the project.

Inside the notebook:

- pretrained depth models are loaded
- RGB images are processed
- depth maps are generated
- results from different models are visualized and compared

The notebook evaluates the following models:

- **MiDaS**
- **DepthAnything**
- **DepthCrafter**

---

# Experiments and Baseline Model Testing

In this project, multiple pretrained depth estimation models were applied to frames extracted from consumer electronics disassembly videos.

The goal was to analyze how well existing depth models perform in **robotic disassembly environments**, which often contain:

- cluttered scenes
- reflective surfaces
- partial occlusions
- varying lighting conditions

The pretrained models were used **without additional training** to establish baseline performance.

---

# Model Comparison

The following pretrained models were tested and compared.

| Model | Description | Observations |
|------|-------------|-------------|
| MiDaS | Monocular depth estimation model widely used as a baseline | Produces stable depth maps but struggles with reflective surfaces |
| DepthAnything | Large-scale pretrained depth model | Generates smoother depth maps with better generalization |
| DepthCrafter | Video-based depth estimation approach | Shows better temporal consistency in sequential frames |

The notebook includes visual comparisons of depth predictions produced by each model.

---

# Depth Estimation Workflow

The general pipeline used in this project is:

```
RGB Image
     ↓
Pretrained Depth Model
(MiDaS / DepthAnything / DepthCrafter)
     ↓
Predicted Depth Map
```

This pipeline allows quick evaluation of how well pretrained models perform on robotic disassembly scenes.

---

# Large Files and Storage Note

Some folders were **not included in this GitHub repository** because they contain very large files (several gigabytes), which exceed GitHub storage limits.

These folders include:

```
depth-capstone/data/
depth-capstone/experiments/
depth-capstone/**/checkpoints/
```

These directories contain:

- datasets
- model checkpoints
- experiment outputs

Due to their large size, they are stored on **HyperGator storage instead of GitHub**.

If access to these files is required, they can be found in the HyperGator project directory:

```
/blue/egn6933/mulakav/
```

---

# How to Navigate the Repository

1. Start with the **Jupyter notebook**

```
Depth_estimation.ipynb
```

This notebook demonstrates how different depth estimation models were applied to the dataset.

2. The **DepthCrafter folder** contains the implementation of one of the evaluated models.

3. The **depth-capstone/scripts folder** contains scripts used to run experiments.

4. Generated logs can be found in:

```
depth-capstone/logs
```

---

# Key Observations

From the baseline experiments:

- Pretrained depth models can produce reasonable depth predictions without additional training.
- However, predictions can still contain noise in complex robotic environments.
- Temporal stability across frames is important for robotics applications.

---

# Future Work

Future improvements for this project include:

- Fine-tuning depth estimation models using robotic disassembly datasets
- Applying self-supervised learning techniques for temporal consistency
- Improving depth stability across sequential frames
- Integrating depth maps into robotic manipulation systems
- Developing an application interface to visualize depth estimation results

---

# Author

**Venkata Jyothi Priya Mulaka**  
M.S. Applied Data Science  
University of Florida
