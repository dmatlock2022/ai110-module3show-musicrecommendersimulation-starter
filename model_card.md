# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0**

---

## 2. Intended Use

VibeMatch is a small classroom music recommender designed to rank songs based on a user's music preferences.

The recommender uses a user's preferred genre, mood, and target energy level to score songs in a small catalog. Songs with higher scores are ranked closer to the top of the recommendation list.

This system is meant for learning and experimentation. It is not intended to replace a real recommendation service such as Spotify or Apple Music.

The model assumes that the user's stated genre, mood, and energy preferences are useful indicators of what they may want to listen to.

---

## 3. How the Model Works

The recommender compares three main song features with the user's preferences:

- Genre
- Mood
- Energy

Each song receives a score.

The final scoring rule is:

- A matching genre adds 1 point.
- A matching mood adds 1.5 points.
- Energy similarity can add up to 2 points depending on how close the song's energy is to the user's target energy.

After all songs are scored, they are ranked from highest score to lowest score. The highest-scoring songs become the recommendations.

The original version gave 2 points for genre and only used energy similarity once. After testing the system, I changed the weights because exact genre matches sometimes had too much influence. The final version gives more importance to mood and energy so songs with a similar overall vibe can rank higher even if the genre does not exactly match.

---

## 4. Data

The recommender uses a small CSV song catalog stored in:

`data/songs.csv`

The original starter dataset contained 10 songs. I expanded the catalog to 15 songs.

Each song includes:

- ID
- Title
- Artist
- Genre
- Mood
- Energy
- Tempo
- Valence
- Danceability
- Acousticness

The catalog includes genres such as pop, indie pop, rock, lofi, jazz, ambient, and synthwave.

It also includes moods such as happy, chill, intense, relaxed, focused, and moody.

The dataset is very small and does not represent the full range of real music. It also does not contain information such as lyrics, language, release year, popularity, or actual user listening behavior.

---

## 5. Strengths

The recommender works well when a user has clear genre, mood, and energy preferences.

During testing, the top recommendation usually matched what I expected.

For the High-Energy Pop profile, Sunrise City ranked first because it matched the user's genre and mood and had an energy value very close to the target.

For the Chill Lofi profile, Library Rain ranked first because it matched the genre, mood, and target energy almost exactly.

For the Intense Rock profile, Storm Runner ranked first because it also matched all three main preferences.

The system also allows songs with a different genre to rank well when their mood and energy are a strong match. This became more noticeable after the scoring weights were adjusted.

---

## 6. Limitations and Bias

The recommender has several limitations.

The song catalog is very small, so it cannot represent the variety of music available in a real recommendation system.

Genre and mood are also simplified into single labels. For example, `pop` and `indie pop` are treated as completely different genres even though they may be related.

The current scoring system does not use:

- Listening history
- Artist preferences
- Lyrics
- Language
- Tempo
- Valence
- Danceability
- Acousticness
- User skips or likes
- Recommendation diversity

The model also uses fixed feature weights. This means the developer decides how important genre, mood, and energy are instead of learning those preferences from each individual user.

The experiment showed that changing the weights can noticeably change the rankings. This means the design of the scoring system can introduce bias by favoring certain features, songs, or types of users.

---

## 7. Evaluation

I evaluated the recommender using three different user profiles.

### High-Energy Pop

- Genre: pop
- Mood: happy
- Energy: 0.8

The top recommendation was Sunrise City.

### Chill Lofi

- Genre: lofi
- Mood: chill
- Energy: 0.35

The top recommendation was Library Rain.

### Intense Rock

- Genre: rock
- Mood: intense
- Energy: 0.9

The top recommendation was Storm Runner.

These results matched my expectations because each top song had a strong combination of genre, mood, and energy similarity.

I also compared two different versions of the scoring rule.

The original version used:

- Genre = 2 points
- Mood = 1.5 points
- Energy = 1 × similarity

The second version used:

- Genre = 1 point
- Mood = 1.5 points
- Energy = 2 × similarity

The second version caused songs with matching mood and energy to move higher even when their genre did not exactly match.

For example, Gym Hero originally ranked second for the High-Energy Pop profile because it matched the pop genre. After lowering the genre weight, happy songs with similar energy moved above it.

Spacewalk Thoughts also moved higher for the Chill Lofi profile because its chill mood and similar energy became more important even though its genre was ambient.

I decided to keep the second scoring rule because it felt less dependent on exact genre matches.

I also ran the automated test suite after making the changes.

Current result:

```text
2 passed
```

---

## 8. Future Work

If I continued developing the recommender, I would add more songs and make the dataset more diverse.

I would also experiment with additional song features such as:

- Tempo
- Valence
- Danceability
- Acousticness

Another improvement would be allowing each user to have their own feature weights instead of giving every user the same scoring rule.

The recommender could also learn from user behavior such as likes, skips, and previous listening history.

I would also improve recommendation diversity so the top results do not become too similar to each other.

---

## 9. Personal Reflection

This project helped me understand that recommendation systems depend heavily on the features and weights chosen by the developer.

Before this project, I mostly thought of music recommendations as simply finding similar songs. After building the scoring system, I saw that even a basic recommender requires decisions about what similarity actually means.

The most interesting part was changing the scoring weights and watching the ranking change. Nothing about the song data changed, but changing the importance of genre and energy caused different songs to move higher or lower.

That showed me how bias can appear in a recommendation system even when the code is simple. The system is not completely objective because its results depend on the decisions made when designing the algorithm.