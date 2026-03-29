import streamlit as st
import pandas as pd
import joblib

#load the trained revised logistic regression model
model = joblib.load("spotify_focus_model.pkl")

#page title and short description
st.title("Spotify Focus Music Predictor")
st.write("Use Spotify audio features to estimate whether a track is likely to be focus-friendly.")

st.info("This tool uses a revised Logistic Regression model trained on Spotify audio features.")

#section heading
st.subheader("Enter Track Feature Values")

#create two columns
col1, col2 = st.columns(2)

with col1:
    acousticness = st.slider(
        "Acousticness",
        min_value=0.0,
        max_value=1.0,
        value=0.50,
        step=0.01
    )

    instrumentalness = st.slider(
        "Instrumentalness",
        min_value=0.0,
        max_value=1.0,
        value=0.50,
        step=0.01
    )

    danceability = st.slider(
        "Danceability",
        min_value=0.0,
        max_value=1.0,
        value=0.50,
        step=0.01
    )

with col2:
    valence = st.slider(
        "Valence",
        min_value=0.0,
        max_value=1.0,
        value=0.50,
        step=0.01
    )

    tempo = st.number_input(
        "Tempo",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    loudness = st.number_input(
        "Loudness",
        min_value=-60.0,
        max_value=0.0,
        value=-10.0,
        step=0.1
    )

#prediction button
st.write("")
if st.button("Generate Prediction"):

    # create a one-row DataFrame with the user inputs
    input_data = pd.DataFrame({
        "acousticness": [acousticness],
        "instrumentalness": [instrumentalness],
        "danceability": [danceability],
        "valence": [valence],
        "tempo": [tempo],
        "loudness": [loudness]
    })

    #make prediction
    prediction = model.predict(input_data)[0]

    #get probability for each class
    prediction_probability = model.predict_proba(input_data)[0]

    #probability of class 1 = focus-friendly
    focus_probability = float(prediction_probability[1])

    #show the result
    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("This track is predicted to be focus-friendly.")
    else:
        st.error("This track is predicted to be non focus-friendly.")

    st.caption("Model Confidence")
    #show probability as a metric
    st.metric("Focus-Friendly Probability", f"{focus_probability:.2%}")

    #show a progress bar for the probability
    st.progress(float(focus_probability))

    st.caption("Higher probabilities indicate a stronger model confidence that the track may support focused listening.")
    st.caption("Note: This probability reflects model confidence, not a guaranteed outcome.")

    #show input summary
    st.subheader("Input Summary")
    st.dataframe(input_data, use_container_width=True)

    #explanation
    st.write("This result is based on the revised Logistic Regression model trained on Spotify audio features.")