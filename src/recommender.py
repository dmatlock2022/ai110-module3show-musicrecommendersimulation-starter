import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the highest-scoring songs for a user."""

        def get_score(song):
            score = 0

            if song.genre == user.favorite_genre:
                score += 2

            if song.mood == user.favorite_mood:
                score += 1.5

            score += 1 - abs(song.energy - user.target_energy)

            return score

        ranked_songs = sorted(
            self.songs,
            key=get_score,
            reverse=True
        )

        return ranked_songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song matches the user's preferences."""
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("genre matches")

        if song.mood == user.favorite_mood:
            reasons.append("mood matches")

        energy_difference = abs(song.energy - user.target_energy)

        if energy_difference <= 0.15:
            reasons.append("energy is close to your preference")

        if not reasons:
            return "This song had one of the higher overall scores."

        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Load song information from a CSV file."""
    songs = []

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])

            songs.append(row)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song based on the user's preferences."""
    score = 0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 2
        reasons.append("genre matches")

    if song["mood"] == user_prefs["mood"]:
        score += 1.5
        reasons.append("mood matches")

    energy_similarity = 1 - abs(
        song["energy"] - user_prefs["energy"]
    )

    score += energy_similarity
    reasons.append(
        f"energy similarity {energy_similarity:.2f}"
    )

    return score, reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Score the songs and return the top recommendations."""
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)

        explanation = ", ".join(reasons)

        scored_songs.append(
            (song, score, explanation)
        )

    scored_songs.sort(
        key=lambda item: item[1],
        reverse=True
    )

    return scored_songs[:k]