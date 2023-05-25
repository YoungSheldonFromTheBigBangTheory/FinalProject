import math, json, random

hexData = []

for i in range(19):
    hexData.append(random.randint(1,3))

#hexType = str(input("Input Correct Answer: "))

Json = {"Type":hexData}

with open("hexType.json", "w") as f:
    f.write(json.dumps(Json))