"""
Create a dictionary mapping five. countries to their capital cities. Iterate
through this dictionary using the items() method and print each pair in the
format: Country -> Capital.
"""

countries = {
    "India": "New Delhi",
    "Japan": "Tokyo",
    "France": "Paris",
    "Australia": "Canberra",
    "Brazil": "Brasília",
}

for country, city in countries.items():
    print(f"{country} -> {city}")
