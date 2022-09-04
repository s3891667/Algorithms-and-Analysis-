# removing the new line characters
with open('./sampleDataToy.txt') as f:
    lines = [line.split() for line in f]
  
for i in range(len(lines)):
    print(lines[i][0])