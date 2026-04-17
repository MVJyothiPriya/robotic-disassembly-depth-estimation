
from pathlib import Path
import streamlit as st
from PIL import Image
import cv2
import numpy as np
import pandas as pd

st.set_page_config(page_title="Depth Estimation Demo", layout="wide")

PROJECT_ROOT = Path("/blue/egn6933/mulakav/depth-capstone")
EVAL_DIR = PROJECT_ROOT / "experiments/eval_900"
RESULTS_DIR = PROJECT_ROOT / "experiments/final_demo_results"

RGB_DIR = EVAL_DIR / "depthcrafter_input_frames"
BASE_DIR = EVAL_DIR / "depth_anything_raw_png"
IMPROVED_DIR = EVAL_DIR / "depth_anything_raw_strongsmooth_png"

summary_csv = RESULTS_DIR / "metrics_summary_baseline_raw_vs_strongsmooth.csv"
base_pf_csv = RESULTS_DIR / "metrics_perframe_baseline_raw.csv"
improved_pf_csv = RESULTS_DIR / "metrics_perframe_baseline_strongsmooth.csv"

summary_compare_2 = pd.read_csv(summary_csv, index_col="model")
base_pf = pd.read_csv(base_pf_csv).set_index("frame")
improved_pf = pd.read_csv(improved_pf_csv).set_index("frame")

base_row = summary_compare_2.loc["DepthAnything_Baseline_Raw"]
improved_row = summary_compare_2.loc["DepthAnything_Baseline_StrongSmooth"]

def read_png01(p):
    x = cv2.imread(str(p), cv2.IMREAD_UNCHANGED)
    if x is None:
        return None
    if x.ndim == 3:
        x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    x = x.astype(np.float32)
    if x.max() > 1.0:
        x = x / 65535.0
    return np.clip(x, 0.0, 1.0)

def fmt(x):
    if pd.isna(x):
        return "N/A"
    if abs(float(x)) < 1e-3:
        return f"{float(x):.6e}"
    return f"{float(x):.6f}"

frames = sorted([p.name for p in RGB_DIR.glob("frame_*.jpg")])

st.title("Depth Estimation Demo")
st.markdown(
    "Finalized model: **DepthAnything + Strong Smoothing**  
"
    "Technique used: **RAW 16-bit depth + Gaussian spatial smoothing + temporal smoothing**"
)

selected = st.selectbox("Select Frame", frames)
frame_num = int(selected.replace("frame_", "").replace(".jpg", ""))

rgb_path = RGB_DIR / selected
base_path = BASE_DIR / selected.replace(".jpg", ".png")
improved_path = IMPROVED_DIR / selected.replace(".jpg", ".png")

rgb = Image.open(rgb_path).convert("RGB")
base = read_png01(base_path)
improved = read_png01(improved_path)

col1, col2, col3 = st.columns(3)

with col1:
    st.image(rgb, caption="RGB Input", use_container_width=True)

with col2:
    if base is not None:
        st.image(base, caption="Baseline DepthAnything (Raw)", use_container_width=True, clamp=True)
    else:
        st.warning("Baseline image missing")

with col3:
    if improved is not None:
        st.image(improved, caption="Final Improved Output (Strong Smoothing)", use_container_width=True, clamp=True)
    else:
        st.warning("Improved image missing")

if frame_num in base_pf.index:
    base_frame_grad = base_pf.loc[frame_num, "grad_mean"]
    base_frame_hf = base_pf.loc[frame_num, "hf_energy_ratio"]
    base_frame_lap = base_pf.loc[frame_num, "lap_mean"]
else:
    base_frame_grad = base_frame_hf = base_frame_lap = np.nan

if frame_num in improved_pf.index:
    improved_frame_grad = improved_pf.loc[frame_num, "grad_mean"]
    improved_frame_hf = improved_pf.loc[frame_num, "hf_energy_ratio"]
    improved_frame_lap = improved_pf.loc[frame_num, "lap_mean"]
else:
    improved_frame_grad = improved_frame_hf = improved_frame_lap = np.nan

st.markdown("## Metrics")

c1, c2 = st.columns(2)

with c1:
    st.markdown("### Overall Average Metrics")
    st.write(f"Baseline Temporal Stability: {fmt(base_row['temporal_mean_absdiff'])}")
    st.write(f"Baseline HF Energy Ratio: {fmt(base_row['hf_energy_ratio_avg'])}")
    st.write(f"Improved Temporal Stability: {fmt(improved_row['temporal_mean_absdiff'])}")
    st.write(f"Improved HF Energy Ratio: {fmt(improved_row['hf_energy_ratio_avg'])}")

with c2:
    st.markdown(f"### Selected-Frame Metrics: {selected}")
    st.write(f"Baseline Grad Mean: {fmt(base_frame_grad)}")
    st.write(f"Baseline Lap Mean: {fmt(base_frame_lap)}")
    st.write(f"Baseline HF Energy Ratio: {fmt(base_frame_hf)}")
    st.write(f"Improved Grad Mean: {fmt(improved_frame_grad)}")
    st.write(f"Improved Lap Mean: {fmt(improved_frame_lap)}")
    st.write(f"Improved HF Energy Ratio: {fmt(improved_frame_hf)}")

st.success("Project decision: finalized model is the improved post-processed output.")
