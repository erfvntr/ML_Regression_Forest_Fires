# Forest Fire Temperature Prediction

Machine learning web application for predicting forest fire temperature based on environmental and fire weather indicators.

## Live Demo

The application is deployed on Render: https://ml-regression-forest-fires-5.onrender.com 


## Project Overview

The model accepts the following input features:

- `FFMC` — Fine Fuel Moisture Code
- `DMC` — Duff Moisture Code
- `DC` — Drought Code
- `ISI` — Initial Spread Index
- `RH` — Relative Humidity
- `Wind` — Wind speed
- `Rain` — Rainfall
- `Area` — Burned area

Based on these values, the trained machine learning model generates a temperature prediction.

The dataset is loaded using the `ucimlrepo` package from the UCI Machine Learning Repository.

## Technologies

The project was developed using:

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn 1.6.1
- SciPy
- Matplotlib
- Seaborn
- ucimlrepo
- Pickle
- HTML
- CSS
- Gunicorn

The application is deployed using Render.

## Installation and Local Run

1. Clone the repository

git clone <https://github.com/erfvntr/ML_Regression_Forest_Fires>

2. Create a virtual environment: python -m venv venv

*  Activate it on Windows: venv\Scripts\activate
*  On macOS or Linux: source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run the application: 

python app.py


## Project Structure

```text
ML_REGRESSION_FOREST_FIRE/
│
├── notebooks/
│   ├── data_loader.py
│   ├── EDA.ipynb
│   ├── train.ipynb
│   └── processed_forest_fires.pkl
│
├── static/
│   ├── forestfires.jfif
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── model_loader.py
├── best_model_full.pkl
├── Procfile
├── requirements.txt
├── README.md
└── .gitignore

Main Files
*  app.py - main Flask application.
*  best_model_full.pkl and processed_forest_fires.pkl - trained machine learning models
*  index.html - HTML structure of the web application and the prediction form
*  style.css - CSS styles used for the web interface
*  EDA.ipynb - exploratory data analysis and visualization of the dataset
*  train.ipynb - data preprocessing, model training, evaluation and selection of the final machine learning model
*  data_loader.py - loads the Forest Fires dataset from the UCI Machine Learning Repository using ucimlrepo.
*  procfile - run the application in production
*  model_loader.py - model path

