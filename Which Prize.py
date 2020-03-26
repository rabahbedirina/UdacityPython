import random as rd
points = rd.randrange(1, 200)

if points <= 50:
    result = "Woden Rabbit"
elif points <= 150:
    result = "No Prize"
elif points <= 180:
    result = "Wafer thin mint"
else:
    result = "Penguin"
if result == "No Prize":
    print("Oh dear, no prize this time.")
else:
    print("Congratulations! \n Your Points {1} You won a {0}!".format(
        result, points))
