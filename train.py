import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv("phishing_site_urls.csv")
df.columns = ["url", "label"]
df = df.drop_duplicates()

X_train, X_test, y_train, y_test = train_test_split(
    df["url"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
)

model = make_pipeline(
    TfidfVectorizer(analyzer="char", ngram_range=(3, 5), max_features=200000),
    LogisticRegression(max_iter=1000),
)
model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))
joblib.dump(model, "model.joblib")