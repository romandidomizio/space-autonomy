# Quick Start Guide

**Goal**: Get the project running in < 5 minutes

---

## 🚀 Fast Setup

### 1. Clone and Enter Directory
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

In Jupyter:
- **Kernel** → **Restart & Run All**
- Wait 2-5 minutes for full execution
- Check for any errors

---

## ✅ Verification Checklist

After running the notebook, you should see:

- [ ] Data loaded (NASA MSL Curiosity Rover P-10 Power Channel)
- [ ] ~1,200 windows created from 6,100 timesteps
- [ ] Class imbalance ~98% normal, 2% anomaly
- [ ] 5 models trained (Dummy, Logistic Regression, RBF SVM, Random Forest, Gradient Boosting)
- [ ] Results table sorted by PR-AUC
- [ ] Best model selected (likely Random Forest or Gradient Boosting)
- [ ] Threshold tuned on validation set
- [ ] Test set evaluation with PR-AUC, ROC-AUC, confusion matrix
- [ ] Feature importance plot
- [ ] Discussion and conclusion

---

## 🧪 Test the Deployed Model

Run this after notebook execution:

```bash
python -c "
from aegisnav_detector import AnomalyDetector
import pandas as pd
import numpy as np

# Create sample telemetry
np.random.seed(42)
telemetry = pd.DataFrame({
    'channel_0': np.random.randn(200),
    'channel_1': np.random.randn(200),
    'channel_2': np.random.randn(200)
})

# Load detector
detector = AnomalyDetector(
    'models/anomaly_detector_pipeline.joblib',
    'models/model_config.json'
)

# Score
results = detector.score_windows(telemetry)
print(f'✓ Scored {len(results[\"probabilities\"])} windows')
print(f'✓ Detected {sum(results[\"predictions\"])} anomalies')
print('✓ Deployment utilities working!')
"
```

Expected output:
```
✓ Scored X windows
✓ Detected Y anomalies
✓ Deployment utilities working!
```

---

## 🔧 Troubleshooting

### Issue: Module import errors
**Solution**: Make sure you installed requirements
```bash
pip install -r requirements.txt
```

### Issue: Notebook kernel crashes
**Solution**: Reduce model complexity or data size
- Edit notebook: Set `n_samples=5000` in synthetic data generation
- Reduce Random Forest `n_estimators` from 200 to 100

### Issue: "No such file or directory" for data
**Solution**: Download MSL data from Kaggle:
```bash
pip install kaggle
kaggle datasets download -d patrickfleith/nasa-anomaly-detection-dataset-smap-msl
unzip nasa-anomaly-detection-dataset-smap-msl.zip -d data/
```

### Issue: Plots not showing
**Solution**: Ensure Jupyter is running with matplotlib backend
```bash
pip install ipympl
# Then in notebook: %matplotlib inline
```

---

## Expected Performance

With the NASA MSL P-10 power channel data:

| Metric      | Expected Range |
|-------------|----------------|
| PR-AUC      | 0.8 - 1.0      |
| ROC-AUC     | 0.9 - 1.0      |
| Test Recall | 0.9 - 1.0      |
| Test Precision | 0.8 - 1.0   |

**Note**: High performance is expected due to the distinct anomaly pattern in the P-10 channel.

---

## 🎯 Next Steps After Verification

1. **Review Results**: Scroll through notebook to understand each section
2. **Modify and Experiment**:
   - Try different window sizes (90, 150)
   - Tune hyperparameters in model grid search
   - Add/remove features
3. **Prepare Video**: Use `VIDEO_GUIDE.md` to plan your presentation
4. **Experiment**: Try different window sizes, thresholds, or other MSL channels
5. **GitHub Setup**: Create public repo and push code

---

## 📁 File Check

After running, you should have:

```
AegisNav-Anomaly-Detection/
├── anomaly_detection_final.ipynb  ✓ (executed with outputs)
├── aegisnav_detector.py           ✓ (created by notebook)
├── models/
│   ├── anomaly_detector_pipeline.joblib  ✓ (created by notebook)
│   └── model_config.json                 ✓ (created by notebook)
├── data/                          (empty or with downloaded data)
├── requirements.txt               ✓
├── README.md                      ✓
├── VIDEO_GUIDE.md                 ✓
├── QUICKSTART.md                  ✓ (this file)
└── .gitignore                     ✓
```

---

## 🆘 Need Help?

1. Check notebook cell outputs for error messages
2. Verify Python version: `python --version` (should be 3.8+)
3. Check scikit-learn version: `python -c "import sklearn; print(sklearn.__version__)"` (should be 1.3+)
4. Re-read the assignment requirements in the notebook introduction

---

## 🎓 Academic Integrity Reminder

Per course guidelines:
- **Critically evaluate** all code before submission
- **Modify and personalize** based on your understanding
- **Document AI usage** if required by your course
- **Understand** every line of code you submit

This notebook provides a foundation - make it yours!

---

**Ready?** Run the notebook and start exploring! 🚀
