# Power Anomaly Detection for Mars Curiosity Rover

**Author**: Roman Di Domizio  
**Course**: CSCA 5622 - Supervised Learning  
**Project**: Final Project

---

## Overview

A supervised binary classification model to detect power subsystem anomalies in NASA's Mars Curiosity Rover telemetry data.

- **Problem**: Classify sliding windows of power readings as normal or anomalous
- **Data**: NASA MSL (Curiosity Rover) P-10 power channel (6,100 timesteps)
- **Methods**: Logistic Regression, RBF SVM, Random Forest, Gradient Boosting (ISLP Chapters 4, 8, 9)
- **Metric**: PR-AUC — appropriate for ~2% anomaly rate

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/romandidomizio/space-autonomy.git
cd space-autonomy/AegisNav-Anomaly-Detection

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run notebook
jupyter notebook anomaly_detection_final.ipynb
```

**Data is included** — no download needed. Just run all cells.

---

## Repository Structure

```
AegisNav-Anomaly-Detection/
├── anomaly_detection_final.ipynb   # Main notebook
├── requirements.txt                # Python dependencies
├── data/                           # NASA P-10 telemetry (included)
│   ├── test/P-10.npy
│   ├── train/P-10.npy
│   └── labeled_anomalies.csv
└── README.md
```

---

## Methods

### Feature Engineering
- Window size: 50 timesteps, stride: 5
- 23 features: statistical, temporal, spectral, derivative

### Models (ISLP Chapters 4, 8, 9)
1. Dummy Classifier (baseline)
2. Logistic Regression (Ch 4)
3. RBF SVM (Ch 9)
4. Random Forest (Ch 8)
5. Gradient Boosting (Ch 8)

---

## References

- Hundman, K., et al. (2018). "Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding." KDD 2018.
- James, G., et al. (2023). *An Introduction to Statistical Learning* (ISLP). Springer.
- NASA Mars Science Laboratory: [mars.nasa.gov/msl](https://mars.nasa.gov/msl/)

---

**GitHub**: https://github.com/romandidomizio/space-autonomy/tree/main/AegisNav-Anomaly-Detection
