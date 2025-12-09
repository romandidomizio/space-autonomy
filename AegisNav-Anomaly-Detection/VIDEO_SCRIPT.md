# Video Demo Script: Power Anomaly Detection for Mars Curiosity Rover

**Target Length**: 7-10 minutes  
**Format**: Screen share walkthrough of Jupyter notebook  
**Style**: Simple, descriptive language — no jargon

---

## Setup Before Recording

1. Open `anomaly_detection_final.ipynb` in Jupyter
2. Run all cells so outputs are visible
3. Collapse code cells if needed to show outputs clearly
4. Have the notebook scrolled to the top (Cell 0)

---

## Script

### [0:00-0:30] Introduction (Cell 0)

*Show Cell 0 - Title and Overview*

"Hello, I'm Roman Di Domizio, and this is my final project for CSCA 5622 Supervised Learning.

I built a machine learning model to detect power anomalies in NASA's Mars Curiosity Rover. The rover has been exploring Mars since 2012, and its power system is critical — if power fails, the mission ends.

This notebook walks through the complete supervised learning workflow: loading real NASA data, exploring it, engineering features, training multiple models, and evaluating performance.

Let me walk you through each section."

---

### [0:30-1:00] Problem Framing (Cell 2)

*Scroll to Cell 2 - Problem Framing*

"In Section 1, I define the problem.

The challenge is that Mars is 4 to 24 minutes away from Earth by radio signal. There's no time for ground control to react to emergencies. The rover needs to detect problems on its own.

My task is binary classification: given a window of power readings, predict whether it's normal or contains an anomaly. I'm using the P-10 power channel because power is the most critical subsystem — no power means no rover."

---

### [1:00-2:00] Data Loading and Cleaning (Cells 3-6)

*Scroll to Cell 4 - Data Loading output*

"Section 2 covers data acquisition. I loaded real telemetry data from NASA's Mars Science Laboratory mission — that's the official name for Curiosity Rover.

The data comes from channel P-10, which is the power subsystem. It has 6,100 timesteps with about 2 percent labeled as anomalous. These labels come from NASA engineers who identified the anomaly segments.

*Scroll to Cell 6 - Data Cleaning output*

In Section 2.2, I check for data quality issues. The data was already clean — no missing values, no infinite values. But I created an additional feature called 'is outlier' that flags extreme values. This could help the model identify unusual readings.

The class imbalance is about 46 to 1 — meaning for every anomaly, there are 46 normal readings. This is important because accuracy would be misleading. A model that always says 'normal' would be 98 percent accurate but useless for detecting anomalies."

---

### [2:00-3:30] Exploratory Data Analysis (Cells 7-10)

*Scroll to Cell 8 output - Class Distribution plots*

"Section 3 is exploratory data analysis, or E-D-A.

The first plot shows the class imbalance visually — almost 6,000 normal readings versus just 131 anomalous ones. The right plot shows when anomalies occur — there's one concentrated region around timestep 4,500.

*Scroll to Cell 9 output - Time Series plots*

This is the key visualization. The top plot shows the full power telemetry stream. For most of the mission, power is stable near 1.0 — that's the normalized maximum.

The bottom plot zooms into the anomaly region. You can see what happened: power was stable, then suddenly it started oscillating wildly between 0.6 and negative 1. After the anomaly, power settled at a lower level around negative 0.7.

This is a real power event from the rover — possibly a battery issue or power distribution problem.

*Scroll to Cell 10 output - ACF and Distribution*

The autocorrelation plot on the left shows that consecutive power readings are highly correlated. This justifies using sliding windows — nearby readings contain useful information.

The distribution plot on the right compares normal versus anomalous readings. Normal readings cluster near 1.0 — high power. Anomalous readings are spread across the entire range, especially at lower values. This visual separation suggests the models should be able to distinguish them."

---

### [3:30-4:30] Feature Engineering (Cells 11-12)

*Scroll to Cell 12 output - Feature creation*

"Section 4 is feature engineering. I convert the raw time series into machine learning features.

I use sliding windows of 50 timesteps, moving 5 steps at a time. This creates about 1,200 training samples from the 6,100 original readings.

For each window, I extract 23 features:
- Statistical features like mean, standard deviation, minimum, and maximum
- Temporal features like the slope and change from first to last value
- Spectral features using Fast Fourier Transform to detect frequency patterns
- And the outlier count from our data cleaning step

If any timestep in a window overlaps with an anomaly, that window is labeled as anomalous."

---

### [4:30-5:00] Train, Validation, Test Split (Cells 13-14)

*Scroll to Cell 14 output - Split summary*

"Section 5 splits the data. I use 60 percent for training, 20 percent for validation, and 20 percent for testing.

There's a challenge: the dataset has only one anomaly segment. With a pure time-based split, all anomalies would end up in one partition. So I use stratified sampling to ensure each split has proportional anomalies — about 3 percent in each.

The standardization is fitted only on training data to prevent data leakage. The same transformation is then applied to validation and test sets."

---

### [5:00-6:00] Model Training (Cells 15-16)

*Scroll to Cell 16 output - Model results table*

"Section 6 trains five models from the ISLP textbook.

First is the Dummy classifier — this just guesses randomly based on class proportions. It's our baseline with a P-R A-U-C of about 0.03.

P-R A-U-C stands for Precision-Recall Area Under Curve. Unlike regular accuracy, it properly handles imbalanced data by focusing on how well we detect the rare positive class.

Logistic Regression from Chapter 4 achieves 0.73. The R-B-F Support Vector Machine from Chapter 9 gets 0.90. Random Forest and Gradient Boosting from Chapter 8 perform best.

Random Forest achieves a perfect 1.0 P-R A-U-C on validation. This seems too good, but remember — the anomaly pattern was very distinct in our E-D-A. The power signal went from stable to chaotic. Features like standard deviation and range easily capture this."

---

### [6:00-6:30] Threshold Tuning (Cells 17-18)

*Scroll to Cell 18 output - PR Curve*

"Section 7 tunes the decision threshold.

By default, models use 0.5 as the cutoff for predicting positive. But for anomaly detection, we want high recall — catching anomalies is more important than avoiding false alarms.

The precision-recall curve shows the tradeoff. I selected a threshold of 0.155 which gives 100 percent recall with 100 percent precision on the validation set."

---

### [6:30-8:00] Test Set Evaluation (Cells 19-20)

*Scroll to Cell 20 output - Test results and confusion matrix*

"Section 8 is the final evaluation on the held-out test set.

The results: P-R A-U-C of 1.0 and R-O-C A-U-C of 1.0.

The confusion matrix tells the full story:
- 235 normal windows correctly classified
- 7 anomalies all detected — that's 100 percent recall
- Just 1 false positive — a normal window incorrectly flagged

The feature importance plot shows which features mattered most. Standard deviation and range are at the top — these capture the volatility during the anomaly. The mean and spectral features also contributed.

The high performance is explained by the distinct anomaly pattern. Normal operation was stable near maximum power. The anomaly showed dramatic fluctuations. Our statistical features easily captured this difference."

---

### [8:00-9:00] Discussion and Conclusion (Cell 21)

*Scroll to Cell 21 - Discussion*

"Section 9 discusses the findings.

Key takeaways:
- Tree-based ensemble methods — Random Forest and Gradient Boosting — outperformed linear models
- The engineered features effectively captured the power anomaly characteristics
- Class imbalance was handled with P-R A-U-C as the primary metric and balanced class weights

Limitations:
- This model uses only one power channel. Correlating multiple channels could improve detection.
- There was only one anomaly segment to learn from. More diverse anomalies would help generalization.
- Window-based features lose precise timing. Sequence models like L-S-T-Ms could capture temporal patterns better.

The project aligns with ISLP Chapters 4, 8, and 9 — covering logistic regression, tree ensemble methods, and support vector machines."

---

### [9:00-9:30] Wrap-Up

*Scroll back to Cell 0 or show GitHub*

"To summarize:

I built a complete supervised learning pipeline for Mars rover power anomaly detection. Starting with real NASA telemetry, I cleaned the data, explored patterns, engineered 23 features, compared 5 models, tuned the threshold, and achieved near-perfect detection on the test set.

The full code is available on GitHub at the link shown in the notebook.

Thank you for watching."

**[END]**

---

## Tips for Recording

1. **Speak slowly and clearly** — aim for 130-150 words per minute
2. **Pause on visualizations** — let viewers read the plots
3. **Point with your cursor** — highlight what you're discussing
4. **Keep energy up** — enthusiasm helps engagement
5. **It's okay to re-record sections** — splice together the best takes

---

## Time Breakdown

| Section | Duration | Cumulative |
|---------|----------|------------|
| Introduction | 0:30 | 0:30 |
| Problem Framing | 0:30 | 1:00 |
| Data Loading/Cleaning | 1:00 | 2:00 |
| EDA | 1:30 | 3:30 |
| Feature Engineering | 1:00 | 4:30 |
| Train/Val/Test Split | 0:30 | 5:00 |
| Model Training | 1:00 | 6:00 |
| Threshold Tuning | 0:30 | 6:30 |
| Test Evaluation | 1:30 | 8:00 |
| Discussion | 1:00 | 9:00 |
| Wrap-Up | 0:30 | 9:30 |

**Total: ~9-10 minutes**
