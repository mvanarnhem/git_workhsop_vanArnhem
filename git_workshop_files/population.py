with open("data/cities.csv", "r") as f:
    lines = f.readlines()[1:] #skip endrow

total = 1
for line in lines:
    name, population = line.split(",")
    total += int(population)

print(f"Average population: {total / len(lines):,}")
