# Spotify Focus Music Analyzer

## Overview
This project explores whether certain Spotify audio features are associated with music that may be better suited for focus or studying.

Using a dataset of Spotify track audio features, the analysis examines characteristics such as acousticness, instrumentalness, energy, speechiness, and tempo. A simple focus score heuristic is created to estimate how suitable a song may be for focus environments.

## Tools Used
- Python
- pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Dataset
This project uses a Spotify tracks dataset containing metadata and audio features for approximately 114,000 tracks.

## Project Workflow
- Loaded and previewed the dataset
- Removed unnecessary index columns
- Explored feature distributions and summary statistics
- Computed a correlation matrix and heatmap
- Built a simple focus score heuristic using acousticness, instrumentalness, energy, and speechiness
- Compared high-scoring and low-scoring tracks
- Ranked tracks using the calculated focus score

## Key Findings
- Tracks ranked highly by the focus score tended to be highly acoustic and strongly instrumental
- High-scoring tracks had much lower energy and speechiness than low-scoring tracks
- Acousticness and energy showed a clear inverse relationship in the dataset
- High-scoring tracks also tended to have slower or more moderate tempos

## Visualizations
### Correlation Heatmap
![Correlation Heatmap](images/correlation_heatmap.png)

### Acousticness vs Energy
![Acousticness vs Energy](images/acousticness_vs_energy.png)

### High vs Low Focus Features
![High vs Low Focus Features](images/high_vs_low_focus_features.png)

## Limitations
The focus score is a simple heuristic based on selected audio features. It does not account for listener preference, lyrical meaning, personal study habits, or whether a track is music versus ambient or white-noise audio.

The goal of the model is to explore how audio feature data can be combined to approximate a focus-oriented listening profile, not to create a definitive recommendation system.

## Files
- `spotify_focus_music_analyzer.ipynb` — main notebook
- `data/spotify_tracks.csv` — dataset
- `images/` — saved visualizations
