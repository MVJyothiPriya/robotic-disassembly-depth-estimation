Robotic Disassembly Depth Estimation
Project Overview

This project explores depth estimation for robotic disassembly tasks using multiple state-of-the-art depth estimation models. The goal is to generate accurate depth maps from RGB images of objects that may appear in robotic manipulation and disassembly environments.

In this project, several pretrained depth estimation models were evaluated, including:

MiDaS

DepthAnything

DepthCrafter

These models were applied to the same dataset to compare their performance and visualize depth predictions.

The experiments and results are documented in the provided Jupyter notebook.

Repository Structure
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
Folder and File Descriptions
DepthCrafter/

Contains the implementation and supporting files for the DepthCrafter depth estimation model.
This model was used as one of the baseline methods for generating depth predictions.
