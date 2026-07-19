from pathlib import Path
import pickle

base_dir = Path(__file__).resolve().parent.parent
model_path = base_dir / "best_model_full.pkl"


def load_model():
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")

    with model_path.open("rb") as file:
        return pickle.load(file)