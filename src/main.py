"""
Command line runner for the Music Recommender Simulation.

This file tests the recommender with several different
user preference profiles.
"""

from src.recommender import load_songs, recommend_songs


def show_recommendations(profile_name, user_prefs, songs):
    print(f"\n{profile_name}")
    print("-" * len(profile_name))

    print(
        f"Genre: {user_prefs['genre']}, "
        f"Mood: {user_prefs['mood']}, "
        f"Energy: {user_prefs['energy']}"
    )

    recommendations = recommend_songs(
        user_prefs,
        songs,
        k=5
    )

    print("\nTop recommendations:\n")

    for song, score, explanation in recommendations:
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


def main():
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8
        },

        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35
        },

        "Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9
        }
    }

    for profile_name, user_prefs in profiles.items():
        show_recommendations(
            profile_name,
            user_prefs,
            songs
        )


if __name__ == "__main__":
    main()