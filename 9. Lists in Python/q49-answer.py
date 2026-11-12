"""
Create a list of 5 of your favourite movies. Print the first, last, and
middle movie from your list using both positive and negative indexing where
appropriate
"""

movies = ["Ramayana", "Dhurandhan", "URI", "Tanhaji", "Border"]

n = len(movies)

print(f"First Movie is = {movies[0]}")

print(f"Last Movie is = {movies[-1]}")

print(f"Middle Indexing Movie is = {movies[n//2]}")
