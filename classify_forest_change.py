from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "forest_change_demo.csv"

FEATURES = [
    "delta_vegetation_index",
    "delta_canopy_estimate",
    "moisture_proxy",
    "disturbance_signal",
]
TARGET = "label"


def main():
    data = pd.read_csv(DATA_PATH)
    X = data[FEATURES]
    y = data[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced",
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print("=== Evaluasi demo pada data sintetis ===")
    print(classification_report(y_test, predictions, zero_division=0))

    # Contoh observasi baru. Angka-angka ini hanya ilustrasi.
    new_observation = pd.DataFrame(
        [{
            "delta_vegetation_index": -0.40,
            "delta_canopy_estimate": -0.36,
            "moisture_proxy": 0.14,
            "disturbance_signal": 0.79,
        }]
    )
    predicted_label = model.predict(new_observation)[0]
    probabilities = model.predict_proba(new_observation)[0]
    probability_by_class = dict(zip(model.classes_, probabilities))

    print("=== Prediksi observasi contoh ===")
    print(f"Label prediksi: {predicted_label}")
    print("Skor model (bukan probabilitas terkalibrasi):")
    for label, score in probability_by_class.items():
        print(f"- {label}: {score:.3f}")

    print("\nCatatan: data dan observasi ini sintetis; hasil tidak menunjukkan kondisi hutan nyata.")


if __name__ == "__main__":
    main()
