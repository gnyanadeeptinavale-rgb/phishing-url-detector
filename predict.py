import joblib

model = joblib.load("model.joblib")
while True:
    url = input("Enter a URL (or 'q' to quit): ")
    if url == "q":
        break
    print("Result:", model.predict([url])[0])