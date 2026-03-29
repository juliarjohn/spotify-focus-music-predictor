# Spotify Focus Music Predictor

This project predicts whether a song is likely to be **focus-friendly** based on its Spotify audio features.

It combines a data analysis workflow with a machine learning model and a simple interactive web app built using Streamlit.

---

## Demo

The app allows users to input audio features such as acousticness, instrumentalness, tempo, and loudness, and returns:

- A prediction (focus-friendly or not)
- A probability score representing model confidence
- A visual confidence bar

---

## Features

- Interactive UI using Streamlit
- Logistic Regression model for classification
- Real-time predictions based on user input
- Probability output using `predict_proba()`
- Clean and simple user interface

---

## How It Works

1. A dataset of Spotify audio features was analyzed and cleaned.
2. Relevant features were selected:
   - acousticness  
   - instrumentalness  
   - danceability  
   - valence  
   - tempo  
   - loudness  
3. A Logistic Regression model was trained to classify tracks as focus-friendly or not.
4. The trained model was saved using `joblib`.
5. The model is loaded into a Streamlit app for real-time predictions.

---

## Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Joblib  

---

## How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/juliarjohn/spotify-focus-music-predictor.git
cd spotify-focus-music-predictor
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
streamlit run app.py
```
---

## Notes

- The probability output represents model confidence, not a guaranteed outcome.
- The model is based only on audio features and does not account for personal listening preferences or context.

---

## Future Improvements

- Improve model calibration for more reliable probability estimates  
- Experiment with additional models (e.g., Random Forest, Gradient Boosting)  
- Add more features such as energy or liveness
- Deploy the app for public access

---

## Project Goal

This project was built to practice:
- data analysis
- feature selection
- machine learning modeling
- deploying models in an interactive application

