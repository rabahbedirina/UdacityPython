names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
username = list()
for i in range(len(names)):
    username.append(names[i].replace(' ', '_').lower())
print(username)


for i in range(len(names)):
    names[i] = names[i].replace(' ', '_').lower()
print(names)
