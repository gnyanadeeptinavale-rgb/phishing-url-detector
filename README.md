# Phishing URL Detector

Machine learning model that classifies URLs as phishing ("bad") or legitimate ("good").

## Dataset
Phishing Site URLs from Kaggle (~550k labeled URLs).

## Method
URLs are converted into character n-gram (3-5) TF-IDF features, then classified with Logistic Regression.

## Results (20% held-out test set, 101,440 URLs)
- Accuracy: 97%
- Phishing precision: 0.97, recall: 0.89
- Legitimate precision: 0.97, recall: 0.99

## How to run
pip install pandas scikit-learn joblib
python train.py
python predict.py

## Future improvements
- Web UI with Streamlit
- Compare with Random Forest
- Add domain-age and WHOIS features