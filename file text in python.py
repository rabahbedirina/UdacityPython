file = open('text.txt', "w")
file.write("""We're the knights of the round table
We dance whenever we're able""")

file.close()

with open('text.txt',) as file:
    data = file.read()

print(data)

with open('text.txt',) as file:
    print(file.read(2))
    print(file.read(8))
    print(file.read(2))
with open('text.txt',) as file:
    print(file.read(2))
    print(file.read(8))
    print(file.read(2))
camelot_lines = []
with open("text.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)
