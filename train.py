import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("dataset/restaurants.csv")

# Encode categorical columns
le_cuisine = LabelEncoder()
le_location = LabelEncoder()

df["Cuisine"] = le_cuisine.fit_transform(df["Cuisine"])
df["Location"] = le_location.fit_transform(df["Location"])

# Target column (dummy example)
df["Recommend"] = [1, 1, 1, 0, 1, 0]

X = df[["Cuisine", "Location", "Rating", "Price"]]
y = df["Recommend"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model/restaurant_model.pkl")

print("Model trained successfully!")
