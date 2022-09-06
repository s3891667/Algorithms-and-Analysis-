import random

# generating input
def writeFile(file, size, command):
    with open('./sampleData200k.txt') as f:
        lines = [line.split() for line in f]
    while (size != 0):
        num = random.randint(0, 199999)
        file.write(command + " " + lines[num][0] + "\n")
        size -= 1
    file.close()


file = open("./testest.in", "w")
writeFile(file, 20, "A")

# generating data
# file = open('./sampleData200k.txt','r').read().splitlines()
# def generatingData(size,data):
#     file = open('data5k.txt','a')
#     while(size!=0):
#       file.write(random.choice(data)+ '\n')
#       size = size-1
#     file.close()
# generatingData(5000,file)
