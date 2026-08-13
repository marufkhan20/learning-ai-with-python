import numpy as np

# Movies Matrix (3 movies x 2 features)
movies = np.array([
    [5, 1],  # Movie A
    [1, 5],  # Movie B
    [4, 4]   # Movie C
])

# Users preferences
users = np.array([
    [5, 1],  # User 1
    [1, 5]   # User 2
])

# 1. Dot products for all movies
dot_products = users @ movies.T

print(f"Dot products: {dot_products}")

# 2. Magnitudes (lengths) of all movies and user
movie_norms = np.linalg.norm(movies, axis=1)  # lengths of each row

print(f"Movie norms: {movie_norms}")

user_norm = np.linalg.norm(users)

print(f"User norm : {user_norm}")

# 3. Cosine similarity formula
similarities = dot_products / (movie_norms * user_norm)

print(f"similarities: {similarities}")

print("Cosine Similarities:", np.round(similarities, 2))