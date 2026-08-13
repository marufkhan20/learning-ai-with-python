# pyrefly: ignore [missing-import]
import numpy as np

# 1. Movie Features [Action, Comedy]
movies = np.array([
    [5, 1],  # Movie A
    [1, 5],  # Movie B
    [4, 4]   # Movie C
])

movie_names = ["Movie A (Action)", "Movie B (Rom-Com)", "Movie C (Action Comedy)"]

# 2. User Preferences [Action, Comedy]
user = np.array([5, 1])

# Calculate preference scores using matrix multiplication
scores = movies @ user

# 3. Find the index of the top recommendation
best_index = np.argmax(scores)

print(f"Scores: {scores}")
print(f"Top Recommendation: 🏆 {movie_names[best_index]}")