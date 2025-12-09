"""
AegisNav Anomaly Detection Deployment Utilities
Author: Roman DiDomizio
"""

import numpy as np
import pandas as pd
import joblib
import json
from pathlib import Path
from scipy import stats
from scipy.fft import fft


class AnomalyDetector:
    """Production anomaly detector for AegisNav Monitor Agent."""

    def __init__(self, model_path, config_path):
        """Load trained pipeline and configuration."""
        self.pipeline = joblib.load(model_path)
        with open(config_path, 'r') as f:
            self.config = json.load(f)

        self.window_size = self.config['window_size']
        self.stride = self.config['stride']
        self.threshold = self.config['decision_threshold']

    def extract_window_features(self, window_data):
        """Extract features from a single telemetry window."""
        features = {}

        # Statistical
        features['mean'] = np.mean(window_data)
        features['std'] = np.std(window_data)
        features['min'] = np.min(window_data)
        features['max'] = np.max(window_data)
        features['median'] = np.median(window_data)
        features['range'] = features['max'] - features['min']

        # Quantiles
        q25, q75 = np.percentile(window_data, [25, 75])
        features['q25'] = q25
        features['q75'] = q75
        features['iqr'] = q75 - q25

        # Distribution shape
        features['skewness'] = stats.skew(window_data)
        features['kurtosis'] = stats.kurtosis(window_data)

        # Temporal
        features['first_value'] = window_data[0]
        features['last_value'] = window_data[-1]
        features['first_last_delta'] = window_data[-1] - window_data[0]

        # Trend
        x = np.arange(len(window_data))
        if len(window_data) > 1:
            slope, _ = np.polyfit(x, window_data, 1)
            features['slope'] = slope
        else:
            features['slope'] = 0

        # Derivatives
        diffs = np.diff(window_data)
        if len(diffs) > 0:
            features['diff_mean'] = np.mean(diffs)
            features['diff_std'] = np.std(diffs)
            features['diff_max'] = np.max(np.abs(diffs))
        else:
            features['diff_mean'] = 0
            features['diff_std'] = 0
            features['diff_max'] = 0

        # Autocorrelation
        if len(window_data) > 1:
            features['lag1_autocorr'] = np.corrcoef(window_data[:-1], window_data[1:])[0, 1]
            if np.isnan(features['lag1_autocorr']):
                features['lag1_autocorr'] = 0
        else:
            features['lag1_autocorr'] = 0

        # Spectral
        if len(window_data) > 4:
            fft_vals = np.abs(fft(window_data))
            fft_vals = fft_vals[:len(fft_vals)//2]
            n_bands = 3
            band_size = len(fft_vals) // n_bands
            for i in range(n_bands):
                start = i * band_size
                end = (i + 1) * band_size if i < n_bands - 1 else len(fft_vals)
                band_energy = np.sum(fft_vals[start:end]**2)
                features[f'fft_band_{i}_energy'] = band_energy
        else:
            for i in range(3):
                features[f'fft_band_{i}_energy'] = 0

        return features

    def score_windows(self, telemetry_df):
        """
        Score telemetry windows for anomaly probability.

        Args:
            telemetry_df: DataFrame with telemetry channels as columns

        Returns:
            dict with 'timestamps', 'probabilities', 'predictions'
        """
        n_samples = len(telemetry_df)
        results = {
            'timestamps': [],
            'probabilities': [],
            'predictions': []
        }

        for start_idx in range(0, n_samples - self.window_size + 1, self.stride):
            end_idx = start_idx + self.window_size
            window = telemetry_df.iloc[start_idx:end_idx]

            # Extract features for all channels
            window_features = {}
            for channel in telemetry_df.columns:
                channel_data = window[channel].values
                channel_features = self.extract_window_features(channel_data)
                for feat_name, feat_val in channel_features.items():
                    window_features[f'{channel}_{feat_name}'] = feat_val

            # Predict
            X_window = pd.DataFrame([window_features])[self.config['feature_names']]
            proba = self.pipeline.predict_proba(X_window)[0, 1]
            pred = int(proba >= self.threshold)

            results['timestamps'].append(telemetry_df.index[start_idx])
            results['probabilities'].append(float(proba))
            results['predictions'].append(pred)

        return results


# Example usage
if __name__ == "__main__":
    detector = AnomalyDetector(
        model_path="models/anomaly_detector_pipeline.joblib",
        config_path="models/model_config.json"
    )

    # Example: Load telemetry and score
    # telemetry = pd.read_csv("telemetry.csv")
    # results = detector.score_windows(telemetry)
    # print(f"Detected {sum(results['predictions'])} anomalies")
