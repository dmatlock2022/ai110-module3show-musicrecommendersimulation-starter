# 🎵 Music Recommender Simulation

## Project Summary

This project is a small music recommender system that compares a user's music preferences with features from a song catalog and ranks songs based on how well they match.

The goal is to show, in a simple way, how recommendation systems turn information about users and items into scores and rankings. The project will also be used to test how changing feature weights can affect recommendations and potentially introduce bias.

For the first version, the recommender mainly uses genre, mood, and energy. Other song features such as tempo, valence, danceability, and acousticness are also included in the dataset and may be used in later experiments.

---

## How The System Works

Real music recommendation systems use information about songs and users to decide what someone may want to listen to next. My simplified recommender compares a user's preferences to song features and gives each song a score.

The song catalog includes:

- Genre
- Mood
- Energy
- Tempo
- Valence
- Danceability
- Acousticness

For the first version of the scoring algorithm, the system uses genre, mood, and energy.

The sample user profile is:

- Favorite genre: pop
- Favorite mood: happy
- Target energy: 0.8

### Algorithm Recipe

Each song starts with a score of 0.

- Add **2 points** if the song's genre matches the user's favorite genre.
- Add **1.5 points** if the song's mood matches the user's favorite mood.
- Add an energy similarity score using:

```text
1 - abs(song energy - target energy)
```

After every song receives a score, the songs are ranked from highest score to lowest score. The highest-scoring songs become the recommendations.

A scoring rule decides how well one individual song matches the user's preferences. A ranking rule compares the scores for all songs and determines the order of the recommendations.

### Basic Flow

```text
User Preferences + Song Catalog
              |
              v
       Score Each Song
              |
              v
        Rank by Score
              |
              v
     Top Recommendations
```

One limitation of this design is that genre and mood receive fixed bonus points, so they may have more influence than other song features. A good song could receive a lower score simply because its genre does not exactly match the user's favorite genre.

Later in the project, I will test different weights and compare how the recommendation results change.

---

## Song Dataset

The song information is stored in:

```text
data/songs.csv
```

Each song includes:

- `id`
- `title`
- `artist`
- `genre`
- `mood`
- `energy`
- `tempo_bpm`
- `valence`
- `danceability`
- `acousticness`

I expanded the starter catalog from 10 songs to 15 songs so the recommender has more options to compare.

---

## Implementation

The main recommendation logic is located in:

```text
src/recommender.py
```

The project currently includes:

- Loading songs from the CSV file
- Converting numerical song values into Python numbers
- Scoring songs based on genre, mood, and energy
- Ranking songs from highest score to lowest score
- Returning the top recommendations
- Providing a short explanation for each recommendation

The command-line runner is located in:

```text
src/main.py
```

---

## Getting Started

### Setup

Create a virtual environment if desired:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Run the Recommender

Run the recommender with:

```bash
python -m src.main
```

---

## Running Tests

The starter project includes automated tests.

Run them with:

```bash
python -m pytest
```

The current tests verify that:

- Songs are ranked by score
- The song that best matches the sample user appears first
- Recommendation explanations return a non-empty string

Current test result:

```text
2 passed
```

---

## Sample Recommendation Output

The first version of the recommendation logic is now implemented using genre, mood, and energy.

```text
User profile:
genre = pop
mood = happy
energy = 0.8

Top recommendations:

Sunrise City - Score: 4.48
Because: genre matches, mood matches, energy similarity 0.98

Gym Hero - Score: 2.87
Because: genre matches, energy similarity 0.87

Open Highway - Score: 2.49
Because: mood matches, energy similarity 0.99

Rooftop Lights - Score: 2.46
Because: mood matches, energy similarity 0.96

Golden Hour - Score: 2.38
Because: mood matches, energy similarity 0.88
```

The current results show how the fixed feature weights affect the ranking. Sunrise City receives the highest score because it matches both the preferred genre and mood while also having an energy level very close to the target.

---

## Experiments You Tried

The first scoring algorithm is now working. The next part of the project will test how the recommendations change when the user profile or feature weights change.

Planned experiments include:

- Changing the genre weight
- Changing the mood weight
- Comparing different target energy values
- Testing different user profiles
- Comparing how the recommendation ranking changes

These experiments will help show how small changes in the scoring rule can strongly affect what the system recommends.

---

## Limitations and Risks

The current recommender has several limitations:

- It uses a very small song catalog.
- Genre and mood are simplified into single labels.
- The system does not understand lyrics.
- It does not learn from actual user listening history.
- Fixed scoring weights may cause certain features to influence the results too strongly.
- Exact genre matches may be favored over songs that a user could still enjoy.
- The recommender does not currently consider diversity in the final recommendation list.
- Some useful song features in the dataset are not yet used by the scoring algorithm.

These limitations will be explored more during the evaluation phase.

---

## Reflection

So far, I have learned that a recommender needs two separate ideas: a scoring rule and a ranking rule. The scoring rule determines how well one item matches a user's preferences, while the ranking rule decides which of those items should appear first.

I also learned that the weights chosen for different features can strongly affect the final result. In the current version, genre receives more weight than mood or energy. This causes songs with a matching genre to receive a large advantage even if another song may have a very similar mood or energy level.

The next part of the project will focus on testing different user profiles and scoring weights to see where the recommender performs well and where its design may introduce bias or unexpected results.

See the model card for the full evaluation and reflection later in the project:

[**Model Card**](model_card.md)