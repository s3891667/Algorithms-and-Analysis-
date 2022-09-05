import random


def writeFile(file, size):
    dataFile = open("./sampleData200k.txt", "r").read().splitlines()
    while (size != 0):
        file.write("AC " + random.choice(dataFile) + "\n")
        size -= 1


file = open("./autocTest.in", "w")
writeFile(file, 20)
