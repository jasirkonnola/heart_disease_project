import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "heart.csv"
if not csv_path.exists():
    csv_path = BASE_DIR.parent / "heart.csv"

if not csv_path.exists():
    raise FileNotFoundError(
        f"Could not find dataset file: {csv_path}.\n"
        "Place heart.csv in the ml directory or the project root, or update the path in train_model.py."
    )

df = pd.read_csv(csv_path)

df = pd.get_dummies(
    df,
    columns=[
        'Sex',
        'ChestPainType',
        'RestingECG',
        'ExerciseAngina',
        'ST_Slope'
    ]
)

X = df.drop('HeartDisease', axis=1)
y = df['HeartDisease']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

joblib.dump(model, "heart_model.pkl")

print("Model Saved")