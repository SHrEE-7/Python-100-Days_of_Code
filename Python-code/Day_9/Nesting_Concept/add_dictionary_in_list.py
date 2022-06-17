travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["paris", "dholkpur", "pandharpur"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["california", "ichal", "kabanoor"],
    },
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["moscow", "saint pitersburg"])
print(travel_log)