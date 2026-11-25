"""
Create a Tuple of 5 of your favourite songs, print the first, last and
middle one using indexing.
"""

songs = ("Pehla Nasha", "Gehra Hua", "Jaan Se Guzarte Hain", "Shararat", "Mangal Rang")

n = len(songs)
print(
    f"First song is = {songs[0]}, middle song is = {songs[n//2]} and last song is = {songs[n-1]}"
)
