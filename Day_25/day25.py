import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")



Fur_Color = ["Gray","Black","Cinnamon"]
counts = []

for color in Fur_Color:
    count=len(data[data["Primary Fur Color"]==color])
    counts.append(count)

dict = {
    "Fur_Color":Fur_Color,
    "Count": counts
}
print(dict)


df = pandas.DataFrame(dict)

print(df)

df.to_csv("Fur_Colors_count.csv")