# Robotic Disassembly Depth Estimation

## Project Overview
This project explores **depth estimation for robotic disassembly tasks** using multiple state-of-the-art depth estimation models. The goal is to generate accurate depth maps from RGB images of objects that may appear in robotic manipulation and disassembly environments.

In this project, several pretrained depth estimation models were evaluated, including:

- **MiDaS**
- **DepthAnything**
- **DepthCrafter**

These models were applied to the same dataset to compare their performance and visualize depth predictions.

The experiments and results are documented in the provided Jupyter notebook.

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
Contains the implementation and supporting files for the **DepthCrafter depth estimation model**.  
This model was used as one of the baseline methods for generating depth predictions.

---

## depth-capstone/
Main project folder containing scripts and experiment setup for the depth estimation experiments.

### scripts/
Contains Python scripts used to:

- load pretrained depth models
- process input images
- generate depth maps
- save results for analysis

### logs/
Contains small log files created during model execution.

---

## Depth_estimation.ipynb
This notebook contains the **main experimental workflow** of the project.

Inside the notebook:

- pretrained models are loaded
- RGB images are processed
- depth maps are generated
- results from different models are visualized and compared

Models tested include:

- **MiDaS**
- **DepthAnything**
- **DepthCrafter**

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

Due to their large size, they are stored on **HyperGator storage** instead of GitHub.

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

2. The **DepthCrafter folder** contains the implementation of one of the tested models.

3. The **depth-capstone/scripts folder** contains scripts used for running the experiments.

4. Generated logs can be found in:

```
depth-capstone/logs
```

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

Initially, pretrained models were used to evaluate baseline performance.

Future work includes **fine-tuning these models on robotic disassembly datasets** to improve performance for this specific domain.

---

# Future Work

Future improvements for this project include:

- Fine-tuning depth estimation models on robotic datasets
- Quantitative evaluation of model performance
- Integrating depth maps into robotic manipulation pipelines
