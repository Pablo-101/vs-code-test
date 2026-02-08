import csv
score = 0
column = 2

with open("csv_file.csv", "r") as file:
    content = csv.reader(file)

    header = next(content)

    for line in content:
        line = float(line[column])
        score += line

print(f"The sum of the 'Score' column is: {score}")
