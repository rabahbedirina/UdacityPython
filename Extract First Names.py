names = ["Rick  Sanchez sggs", "Morty Smith",
         "Summer Smith", "Jerry Smith", "Rabah Smith rabah

first_names = [name.lower()[:name.find(" ")] for name in names]
print(first_names)
first_names = [name.lower()[:name.index(" ")] for name in names]
print(first_names)
first_names = [name.lower().split(" ")[0] for name in names]
print(first_names)
