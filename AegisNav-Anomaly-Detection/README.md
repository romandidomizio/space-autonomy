# Power Anomaly Detection for Mars Curiosity Rover

**Author**: Roman Di Domizio  
**Course**: CSCA 5622 - Supervised Learning  
**Project**: Final Project

---

## Overview

A supervised binary classification model to detect power subsystem anomalies in NASA's Mars Curiosity Rover telemetry data.

**Problem**: Classify sliding windows of power readings as normal or anomalous  
**Data**: NASA Mars Science Laboratory (Curiosity Rover) P-10 power channel (6,100 timesteps)  
**Methods**: Logistic Regression, RBF SVM, Random Forest, Gradient Boosting (ISLP Chapters 4, 8, 9)  
**Metric**: PR-AUC (primary) — appropriate for ~2% anomaly rate

---

## 📁 Repository Structure

```
AegisNav-Anomaly-Detection/
├── anomaly_detection_final.ipynb    # Main notebook (EDA, modeling, evaluation)
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── data/                            # Telemetry data (download separately)
└── .gitignore
```

---

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/romandidomizio/space-autonomy.git
cd space-autonomy/AegisNav-Anomaly-Detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Notebook

```bash
jupyter notebook anomaly_detection_final.ipynb
```

### 4. Download Data

See [Data Acquisition](#-data-acquisition) section below for Kaggle download instructions.

---

## 🔬 Methods Summary

### Feature Engineering
- **Window Size**: 50 timesteps
- **Stride**: 5 timesteps (90% overlap)
- **Feature Types**: Statistical, temporal, spectral (FFT), derivative, outlier flags
- **Total Features**: 23 features per window

### Models Evaluated (ISLP Chapters 4, 8, 9)
1. Dummy Classifier (baseline)
2. Logistic Regression (Chapter 4)
3. RBF Support Vector Machine (Chapter 9)
4. Random Forest (Chapter 8)
5. Gradient Boosting (Chapter 8)

### Evaluation Strategy
- **Stratified splits**: 60% train, 20% validation, 20% test (stratified due to single anomaly segment)
- **Primary metric**: PR-AUC (handles class imbalance)
- **Threshold tuning**: Target 80% recall on validation set
- **Segment-level detection**: Count true positive if any window triggers during anomaly segment

---

## References

**Primary Data Source**:
- Hundman, K., et al. (2018). "Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding." *KDD 2018*. [arXiv:1802.04431](https://arxiv.org/abs/1802.04431)
- Telemanom Repository: [khundman/telemanom](https://github.com/khundman/telemanom)

**Textbook**:
- James, G., et al. (2023). *An Introduction to Statistical Learning with Applications in Python* (ISLP). Springer.

**NASA Mission**:
- [Mars Science Laboratory (Curiosity Rover)](https://mars.nasa.gov/msl/)

---

## 📝 Data Acquisition

### NASA MSL (Curiosity Rover) Telemetry

The dataset contains real telemetry from NASA's Curiosity Rover, collected and labeled by NASA Jet Propulsion Laboratory (JPL).

**Download from Kaggle**:
```bash
# Install Kaggle CLI
pip install kaggle

# Download dataset
kaggle datasets download -d patrickfleith/nasa-anomaly-detection-dataset-smap-msl
unzip nasa-anomaly-detection-dataset-smap-msl.zip -d data/
```

**Data Structure**:
```
data/
├── train/P-10.npy    # Training data (not used - no anomaly labels)
├── test/P-10.npy     # Test data with labeled anomalies (6,100 samples)
└── labeled_anomalies.csv  # Anomaly segment indices
```

**Channel P-10 Details**:
- Spacecraft: Mars Science Laboratory (Curiosity Rover)
- Subsystem: Power
- Samples: 6,100 timesteps
- Anomaly Rate: ~2.1%

---

## 🙏 Acknowledgments

- NASA Jet Propulsion Laboratory for Mars Science Laboratory telemetry
- Hundman et al. for the Telemanom benchmark and anomaly labeling
- ISLP authors for foundational supervised learning methods
- CSCA 5622 course staff for guidance

---

## 📧 Contact

Roman Di Domizio - [GitHub](https://github.com/romandidomizio)

**Project Repository**: [GitHub](https://github.com/romandidomizio/space-autonomy/tree/main/AegisNav-Anomaly-Detection)
