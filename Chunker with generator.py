def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""

    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


for chunk in chunker(range(25), 4):
    print(list(chunk))

sq_list = [x**2 for x in range(10)]  # this produces a list of squares
print(sq_list)
sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
print(list(sq_iterator))
