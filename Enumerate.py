cast = ["Barney Stinson", "Robin Scherbatsky",
        "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, cas in enumerate(cast):
    cast[i] = cas + ' ' + str(heights[i])


print(cast)
