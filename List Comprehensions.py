cities = ["Barney Stinson", "Robin Scherbatsky",
          "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.lower())

print(capitalized_cities)
capitalized_cities = [city.lower() for city in cities]

print(capitalized_cities)

squares = [x ** 2 for x in range(9)]
print(squares)
squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)
squares = [x ** 2 for x in range(9) if x % 2 != 0]
print(squares)
squares = [x**2 if x % 2 == 0 else x for x in range(9)]
print(squares)

scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98
}

# write your list comprehension here

passed = [score if score >= 70 and score <
          85 else 0 for name, score in scores.items()]
print(passed,)


x = y = z = n = 3


print([[i, j, k] for i in range(x+1) for j in range(y+1)
       for k in range(z+1) if ((i + j+k) != n)])
