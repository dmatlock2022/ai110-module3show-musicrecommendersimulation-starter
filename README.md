# 🎵 Music Recommender Simulation

## Project Summary

This project is a small music recommender system that compares a user's music preferences with features from a song catalog and ranks songs based on how well they match.

The goal is to show, in a simple way, how recommendation systems turn information about users and items into scores and rankings. The project also demonstrates how changing feature weights can change recommendation results and introduce bias into a system.

The final version of the recommender mainly uses genre, mood, and energy. Other song features such as tempo, valence, danceability, and acousticness are included in the dataset but are not currently used in the scoring rule.

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

The current scoring algorithm uses:

- Genre
- Mood
- Energy

### User Profile

A user profile contains:

- Favorite genre
- Favorite mood
- Target energy level

One example profile is:

- Favorite genre: pop
- Favorite mood: happy
- Target energy: 0.8

### Algorithm Recipe

Each song starts with a score of 0.

- Add **1 point** if the song's genre matches the user's favorite genre.
- Add **1.5 points** if the song's mood matches the user's favorite mood.
- Add an energy similarity score using:

```text
2 * (1 - abs(song energy - target energy))
```

After every song receives a score, the songs are ranked from highest score to lowest score. The highest-scoring songs become the recommendations.

A scoring rule decides how well one song matches the user's preferences. A ranking rule compares the scores for all songs and determines which recommendations appear first.

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

---

## Song Dataset

The song catalog is stored in:

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

The original starter catalog contained 10 songs. I expanded it to 15 songs so the recommender would have more examples to compare.

The dataset contains songs from genres such as:

- Pop
- Indie pop
- Rock
- Lofi
- Jazz
- Ambient
- Synthwave

The moods include examples such as:

- Happy
- Chill
- Intense
- Relaxed
- Focused
- Moody

---

## Implementation

The main recommendation logic is located in:

```text
src/recommender.py
```

The project currently includes:

- Loading songs from a CSV file
- Converting numerical CSV values into Python numbers
- Representing songs and user profiles as data
- Scoring songs based on genre, mood, and energy
- Ranking songs from highest score to lowest score
- Returning the top recommendations
- Explaining why songs received their recommendations

The command-line runner is located in:

```text
src/main.py
```

The current version tests the recommender with several different user profiles.

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

Run the automated tests with:

```bash
python -m pytest
```

The current tests verify that:

- Songs are ranked based on their scores
- A song that strongly matches a user's preferences ranks above a weak match
- Recommendation explanations return a non-empty string

Current test result:

```text
2 passed
```

---

## Sample Recommendation Output

One test profile uses:

```text
genre = pop
mood = happy
energy = 0.8
```

The final scoring system produced:

```text
High-Energy Pop
---------------
Genre: pop, Mood: happy, Energy: 0.8

Top recommendations:

Sunrise City - Score: 4.46
Because: genre matches, mood matches, energy similarity 0.98

Open Highway - Score: 3.48
Because: mood matches, energy similarity 0.99

Rooftop Lights - Score: 3.42
Because: mood matches, energy similarity 0.96

Golden Hour - Score: 3.26
Because: mood matches, energy similarity 0.88

Gym Hero - Score: 2.74
Because: genre matches, energy similarity 0.87
```

Sunrise City received the highest score because it matches both the preferred genre and mood while also having an energy level very close to the user's target.

---

## Evaluation Profiles

I tested the recommender using three different user profiles.

### High-Energy Pop

```text
Genre: pop
Mood: happy
Energy: 0.8
```

Top result:

```text
Sunrise City
```

This result made sense because Sunrise City matched the preferred genre, mood, and energy closely.

### Chill Lofi

```text
Genre: lofi
Mood: chill
Energy: 0.35
```

Top results included:

```text
Library Rain
Midnight Coding
Spacewalk Thoughts
```

Library Rain ranked first because it matched the lofi genre, chill mood, and target energy almost exactly.

Spacewalk Thoughts also ranked highly even though it is ambient instead of lofi because its mood and energy were close to the user's preferences.

### Intense Rock

```text
Genre: rock
Mood: intense
Energy: 0.9
```

Top results included:

```text
Storm Runner
Electric Rush
Gym Hero
```

Storm Runner ranked first because it matched all three main preferences.

Electric Rush and Gym Hero also ranked highly because their intense mood and energy were strong matches even though their genres were different.

---

## Experiments You Tried

The original scoring rule was:

```text
Genre match = 2 points
Mood match = 1.5 points
Energy = 1 × similarity
```

This version produced reasonable recommendations, but genre had more influence than I expected.

For example, Gym Hero originally ranked second for the High-Energy Pop profile because it matched the pop genre even though its mood was intense instead of happy.

I then tested a second scoring rule:

```text
Genre match = 1 point
Mood match = 1.5 points
Energy = 2 × similarity
```

The second version gave more importance to mood and energy.

For the High-Energy Pop profile, happy songs with similar energy moved above Gym Hero.

For the Chill Lofi profile, Spacewalk Thoughts moved higher because its chill mood and energy matched closely even though it was not a lofi song.

For the Intense Rock profile, Electric Rush and Gym Hero moved above Open Highway because they matched the user's mood and energy more closely.

I decided to keep the second scoring rule because it felt less dependent on exact genre matches and allowed songs with a similar overall vibe to rank more highly.

---

## Strengths

The current recommender works well when:

- The user has clear genre, mood, and energy preferences
- A song matches multiple preferences
- Songs have noticeably different feature values
- The goal is to find songs with a similar general vibe

The ranking also reacts predictably when feature weights are changed.

---

## Limitations and Risks

The recommender has several limitations:

- It uses a very small song catalog.
- Genre and mood are simplified into single labels.
- The system does not understand lyrics.
- It does not use actual listening history.
- It does not learn from user feedback.
- It does not consider artists the user already likes.
- Tempo, valence, danceability, and acousticness are currently ignored by the scoring rule.
- Exact labels such as `pop` and `indie pop` are treated as different genres.
- Fixed feature weights may favor certain types of users or songs.
- The recommender does not currently enforce diversity among the top recommendations.

The weight experiment also showed that recommendations can change significantly based on small design decisions. This means the developer's choices can introduce bias into the ranking.

---

## Reflection

This project helped me understand that a recommender system does more than simply find songs that match a user's favorite genre. The system needs a scoring rule that decides which features matter and how important each one should be.

I also learned that scoring and ranking are separate steps. First, each song receives a score. Then the system compares those scores and ranks the songs.

The most interesting part was seeing how much the recommendations changed when I adjusted the weights. The first version favored exact genre matches more heavily, while the second version gave more importance to mood and energy. Neither version is automatically correct. The results depend on what the designer decides should matter.

This made it clear that recommendation systems can contain bias even when the code itself is simple. The choices made when selecting features and weights directly affect what users are shown.

See the model card for the full evaluation and reflection:

[**Model Card**](model_card.md)