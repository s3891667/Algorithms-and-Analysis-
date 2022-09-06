import matplotlib.pyplot as plt

# search
# 500   1k   5k    10k   20k   50k   100k
# kinda the same with trie
array = [0.42,1.20,3.92,14.03,32.73,133.51,331.29]
trie = [0.08,0.13,0.19,0.17,0.17,0.19,0.20]
#take more time
linkedList = [1.37,2.41,12.11,13.38,27.22,62.75,128.23]


# add
# array = [0.82, 2.0, 7.72, 17.82, 37.42, 163.33, 313.36]
# trie= [0.37, 0.35, 0.39, 0.38, 0.4, 0.44, 0.4]
# linkedList = [1.43, 2.81, 14.4, 15.33, 30.8, 76.71, 136.92]

# delete
# array = [0.99, 1.14, 6.62, 14.18, 23.82, 162.13, 318.24]
# trie = [0.15, 0.14, 0.18, 0.22, 0.13, 0.20, 0.21]
# linkedList = [1.62, 3.08, 8.48, 17.33, 35.23, 81.38, 154.26]

# autocomplete
# array = [2.37, 3.02, 16.97, 94.25, 308.58, 2063.87, 6304.30]
# trie = [0.53, 0.79, 3.31, 3.88, 11.32, 18.32, 28.29]
# linkedList = [2.06, 4.29, 32.48, 93.36, 170.37, 1021.30, 5812.17]

array = [x/20 for x in array]
trie  = [x/20 for x in trie]
linkedList = [x/20 for x in linkedList]
data_size = ["500", "1k", "5k" , "10k", "20k", "50k", "100k"]

plt.plot(data_size, array, "r-")
plt.plot(data_size, trie, "b-")
plt.plot(data_size, linkedList, "g-")
plt.xlabel('Dataset sizes')
plt.ylabel('Execution time per operation (ms)')
plt.title('Search word-frequency')
plt.show() 