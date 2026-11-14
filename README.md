# 🎵 Music Recommender Simulation

## Project Summary

This project is a small music recommender system that will compare a user's music preferences with features from a song catalog and rank songs based on how well they match.

The goal is to show, in a simple way, how recommendation systems turn information about users and items into scores and rankings. The project will also be used to test how changing feature weights can affect recommendations and potentially introduce bias.

For the first version, the recommender will mainly use genre, mood, and energy. Other song features such as tempo, valence, danceability, and acousticness are also included in the dataset and may be used in later experiments.

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

For the first version of the scoring algorithm, I will use genre, mood, and energy.

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

One limitation of this design is that genre and mood receive fixed bonus points, so they may have more influence than other features. A good song could receive a lower score simply because its genre does not exactly match the user's favorite genre.

Later in the project, I will test different weights and compare how the recommendation results change.

---

## Song Dataset

The starter dataset contains song information stored in:

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

I expanded the starter catalog so the recommender has more songs to compare when the scoring system is implemented.

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

### Run the App

Once the recommendation logic is implemented, run:

```bash
python -m src.main
```

---

## Running Tests

The starter project includes automated tests.

Run them with:

```bash
pytest
```

Additional tests will be added as the recommendation algorithm is implemented.

---

## Sample Recommendation Output

The recommendation logic has not been implemented yet.

A later version will produce output similar to:

```text
User profile:
genre = pop
mood = happy
energy = 0.8

Top recommendations:
1. Song title - Score: ...
2. Song title - Score: ...
3. Song title - Score: ...
```

This section will be updated after the recommender is working.

---

## Experiments You Tried

Experiments will be added after the first scoring algorithm is implemented.

Planned experiments include:

- Changing the genre weight
- Changing the mood weight
- Comparing different target energy values
- Testing different user profiles
- Comparing how the recommendation ranking changes

These experiments will help show how small changes in the scoring rule can strongly affect what the system recommends.

---

## Limitations and Risks

The current design has several limitations:

- It uses a very small song catalog.
- Genre and mood are simplified into single labels.
- The system does not understand lyrics.
- It does not learn from actual user listening history.
- Fixed scoring weights may cause certain features to influence the results too strongly.
- Exact genre matches may be favored over songs that a user could still enjoy.
- The recommender does not yet account for the diversity of the final recommendation list.

These limitations will be explored more as the recommendation algorithm is tested.

---

## Reflection

The full project reflection will be completed later after the recommender has been implemented and tested.

So far, I have learned that a recommender needs two separate ideas: a scoring rule and a ranking rule. The scoring rule determines how well one item matches a user's preferences, while the ranking rule decides which of those items should appear first.

I also learned that the weights chosen for different features can strongly affect the result. Even a simple rule such as giving extra points for genre can cause the system to repeatedly favor certain types of music. This means that recommendation systems are influenced by the choices made when designing their algorithms.

See the model card for the full evaluation and reflection later in the project:

[**Model Card**](model_card.md)