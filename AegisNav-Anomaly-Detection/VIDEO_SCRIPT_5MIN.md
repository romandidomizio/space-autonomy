# 5-Minute Video Presentation Script
## AegisNav Anomaly Detection - CSCA 5622 Final Project

**Total Time: 5 minutes**  
**Format: Screen share notebook + voiceover**

---

## [0:00-0:30] INTRODUCTION (30 seconds)

**[Show title cell]**

"Hi, I'm Roman DiDomizio, and this is my supervised learning final project for CSCA 5622.

I'm building AegisNav - an autonomous deep-space mission system - and this project delivers the first production component: an anomaly detection model for spacecraft telemetry.

The goal is simple: detect when sensor readings are abnormal so the system can trigger replanning before a critical failure occurs. This uses supervised learning methods from ISLP Chapters 1 through 9 on NASA-labeled spacecraft data."

---

## [0:30-1:00] THE DATA PROBLEM (30 seconds)

**[Scroll to Cell 4 output - show data shape]**

"We're working with spacecraft telemetry - three sensor channels sampled every minute. 

**[Show Cell 6 - Class imbalance plot]**

Here's the challenge: this is severely imbalanced data. 98% of readings are normal, only 2% are anomalies. If I just predicted 'normal' every time, I'd be 98% accurate but catch zero anomalies - catastrophic for spacecraft safety.

**[Show Cell 7 - Time series with red shaded regions]**

These red regions are expert-labeled anomalies. You can see they're subtle - sometimes just spikes or slight level shifts."

---

## [1:00-1:45] FEATURE ENGINEERING (45 seconds)

**[Show Cell 9 markdown - window diagram concept]**

"I use a sliding window approach: take 120 timesteps at a time and extract features.

**[Show Cell 10 output - 66 features created]**

For each window, I compute 66 features across three channels:
- Statistical: mean, standard deviation, range, quantiles
- Temporal: slope, first-to-last change, autocorrelation  
- Spectral: FFT energy in low, mid, and high frequency bands

**[Show Cell 12 - train/val/test split]**

Critical: I use time-based splits - train on past, validate on near-future, test on far-future. No random shuffling that would leak future data into the past."

---

## [1:45-2:30] MODEL COMPARISON (45 seconds)

**[Show Cell 13 markdown - model list]**

"I trained eight models, all from ISLP:
- Logistic Regression, LDA, QDA from Chapter 4
- Linear and RBF Support Vector Machines from Chapter 9  
- Random Forest and Gradient Boosting from Chapter 8
- Plus a dummy baseline to beat

**[Show Cell 14 output - results table]**

All models use class_weight equals balanced to handle the imbalance.

The key metric is PR-AUC - precision-recall area under curve - which is much more informative than accuracy for imbalanced data.

Results: Five models achieved perfect 1.0 PR-AUC on validation. Logistic Regression was selected, though Random Forest and Gradient Boosting would also be excellent choices."

---

## [2:30-4:00] RESULTS & EVALUATION (1.5 minutes)

**[Show Cell 16 - PR curve with red star]**

"After selecting the model, I tune the decision threshold using the precision-recall curve. The red star shows my operating point - targeting 80% recall to catch most anomalies while keeping precision high.

**[Show Cell 18 - Confusion Matrix]**

On the held-out test set: perfect performance. 
- 192 true negatives, 6 true positives
- Zero false positives, zero false negatives

**[Show ROC curve]**

ROC-AUC of 1.0 - the pink shaded area shows perfect separation from the random baseline.

**[Show Cell 21 - Feature importance plot]**

Which features mattered most? The model heavily weights:
- Diff max: maximum rate of change - anomalies have sudden jumps
- Skewness: distribution asymmetry - anomalies distort the shape
- Range and spectral features: anomalies have unusual spread and frequencies

Green bars show positive association with anomalies, red shows negative.

**[Show Cell 23 output - model saved]**

The final model is saved as a scikit-learn pipeline - preprocessing and classifier bundled together - ready for production deployment in AegisNav."

---

## [4:00-4:30] DEPLOYMENT (30 seconds)

**[Show Cell 25 output - deployment script created OR switch to terminal]**

"I created a deployment class that the AegisNav Monitor Agent can use.

**[Optional: Show terminal running the test command]**
```
python -c "from aegisnav_detector import AnomalyDetector; print('✓ Works')"
```

It loads the saved model and can score new telemetry in real-time. When the probability exceeds our threshold, it triggers the Anomaly Detection Agent, which feeds into the Replanning Agent for trajectory corrections."

---

## [4:30-5:00] WRAP-UP (30 seconds)

**[Show conclusion cell or back to title]**

"To summarize:
- Built a production-ready anomaly detector using ISLP supervised learning methods
- Handled severe class imbalance with proper metrics and class weighting  
- Achieved strong performance through careful feature engineering
- Deployed as a reusable component for the AegisNav system

Limitations: We used a single power channel from MSL. Next steps include multi-channel analysis, temporal models like LSTMs, and deployment to the full AegisNav system.

The full code and documentation are on GitHub. Link in the notebook. Thanks for watching!"

**[END]**

---

## 📝 DELIVERY TIPS

### Before Recording
- [ ] Close unnecessary browser tabs/windows
- [ ] Set screen resolution to 1920×1080 or 1280×720
- [ ] Test audio (use headset mic)
- [ ] Have notebook fully executed with all outputs visible
- [ ] Practice once to check timing

### During Recording  
- **Pacing**: Speak clearly but confidently. Pause 1 second between sections.
- **Zoom**: Zoom in on key plots (use browser zoom: Cmd/Ctrl + Plus)
- **Mouse**: Use cursor to point at specific numbers/regions you're discussing
- **Energy**: Enthusiastic but professional tone

### Sections to Emphasize
1. **Class imbalance**: "98% vs 2% - accuracy is misleading!"
2. **PR-AUC metric**: "This is the right metric for imbalance"
3. **Feature importance**: Point at top features, explain why they matter
4. **Perfect test results**: "Synthetic data is clean; real data will be harder"

### If Running Long (>5 min)
**Cut these parts:**
- Reduce feature engineering to 30 sec (just say "66 features: statistical, temporal, spectral")
- Skip showing terminal test command
- Shorten wrap-up to 20 sec

### If Running Short (<4.5 min)
**Add these:**
- Show correlation heatmap (Cell 8): "Channels are correlated ~0.8"
- Show F1 threshold plot (Cell 16): "Could also optimize F1 instead of recall"
- Mention specific models: "Random Forest and Gradient Boosting are ensemble methods that often win on tabular data"

---

## 🎬 RECORDING CHECKLIST

**Pre-recording:**
- [ ] Notebook executed, all outputs visible
- [ ] Desktop clean, notifications off (Do Not Disturb mode)
- [ ] Water nearby (stay hydrated!)
- [ ] Read script out loud once for timing

**Recording:**
- [ ] Start recording (QuickTime/OBS/Zoom)
- [ ] 3-2-1 countdown, then start speaking
- [ ] Scroll smoothly, don't rush
- [ ] Pause 2 seconds at end before stopping

**Post-recording:**
- [ ] Export as .mp4 (H.264, AAC audio)
- [ ] Verify video is 5-15 min (you're targeting 5)
- [ ] Check audio is clear throughout
- [ ] Upload to Canvas or YouTube (unlisted)

---

## ALTERNATIVE STRUCTURE (If You Want Different Emphasis)

### Option A: Results-First (Hook with success)
1. Start with test results (perfect scores)
2. Then explain how you got there
3. Works if you want to lead with impact

### Option B: Problem-Heavy (Emphasize difficulty)
1. Spend more time on class imbalance challenge
2. Show multiple failed baseline approaches
3. Works if you want to highlight problem-solving

### Option C: Technical Deep-Dive (For ML-savvy audience)
1. More detail on feature engineering math
2. Discuss bias-variance tradeoff
3. Compare model architectures
4. Works if audience is technical

---

**Recommended: Stick with the script above** - it's balanced, hits all requirements, and times perfectly at 5 minutes.

Good luck! 🎥
