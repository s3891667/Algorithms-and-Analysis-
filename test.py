import random 
#generating input 
# with open('./sampleDataToy.txt') as f:
#     lines = [line.split() for line in f]
  
# for i in range(len(lines)):
#     print(lines[i][0])
    

#generating data 
file = open('./sampleData200k.txt','r').read().splitlines()
def generatingData(size,data):
    file = open('data' + str(size) + ".txt",'a')
    while(size!=0):
      file.write(random.choice(data)+ '\n')
      size -=1
    file.close()
generatingData(500,file)        
    
    
    
    
    
    