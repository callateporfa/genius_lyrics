import pandas as pd
data = pd.read_json("lyrics.jl", lines=True)
counter = 0
numofns = []
lyrics = data["lyrics"].tolist()
for i in lyrics:
    lenghthh = len(i.split("\n"))
    numofns.append(lenghthh)
print(numofns)
