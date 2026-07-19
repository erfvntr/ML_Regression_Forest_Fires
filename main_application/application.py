from pathlib import Path
import webbrowser
from threading import Timer
import pandas as pd
from flask import Flask, render_template, request
from model_loader import load_model


base_dir = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    template_folder=str(base_dir / "templates"),
    static_folder=str(base_dir / "static")
)

saved_data = load_model()
model = saved_data["model_pipeline"]


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")
    
    
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", prediction=None, error=None)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = {
            "ffmc": float(request.form["ffmc"]),
            "dmc": float(request.form["dmc"]),
            "dc": float(request.form["dc"]),
            "isi": float(request.form["isi"]),
            "rh": int(request.form["rh"]),
            "wind": float(request.form["wind"]),
            "rain": float(request.form["rain"]),
            "area": float(request.form["area"])
        }

        input_df = pd.DataFrame([input_data])
        prediction = float(model.predict(input_df)[0])

        return render_template(
            "index.html",
            prediction=prediction,
            error=None
        )

    except Exception as error:
        return render_template(
            "index.html",
            prediction=None,
            error=f"Prediction failed: {error}"
        )


if __name__ == "__main__":
    Timer(1, open_browser).start()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        use_reloader=False
    )